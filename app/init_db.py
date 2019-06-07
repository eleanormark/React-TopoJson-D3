import csv
import sys
import gzip

from collections import defaultdict

from www import models

ROUGH_ROW_COUNT = 2000000


def stdout(text):
    print(text)
    sys.stdout.flush()


def parse_file(infile):
    reader = csv.DictReader(infile)
    physicians = defaultdict(int)
    specialties = defaultdict(int)

    count = 0

    for row in reader:
        specialty = row['specialty']
        state = row['state']

        if not state:
            raise ValueError(row)

        if specialty:
            physicians[(specialty, state)] += 1
            specialties[specialty] += 1

        physicians[(None, state)] += 1

        count += 1
        if count % 100000 == 0:
            stdout("Parsed {count}k/~{total}k rows".format(
                count=int(count / 1000),
                total=int(ROUGH_ROW_COUNT / 1000)
            ))

    return physicians, specialties


def write_physicians(session, physicians):
    session.query(models.Physicians).delete()

    for (specialty, state), count in physicians.items():
        session.add(models.Physicians(specialty=specialty, state=state, count=count))

    session.commit()


def write_specialties(session, specialties):
    session.query(models.Specialties).delete()

    for specialty, count in specialties.items():
        session.add(models.Specialties(specialty=specialty, count=count))

    session.commit()


if __name__ == '__main__':

    stdout("Reading source file")
    with gzip.open(sys.argv[1], 'rt') as infile:
        physicians, specialties = parse_file(infile)

    stdout("Creating sqlite tables")
    engine = models.sqlite_engine()
    models.create_tables(engine)
    session = models.get_session(engine)

    stdout("Writing database entries")
    write_physicians(session, physicians)
    write_specialties(session, specialties)
