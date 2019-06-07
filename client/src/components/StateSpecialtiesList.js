import React from 'react';
import {Container, Header, Table} from "semantic-ui-react";

function StateSpecialties(props) {
  let list = [];
  for (let i =0; i < props.stateSpecialties.length; i++) {
    if (props.stateSpecialties[i].specialty){
      list.push(
        <Table.Row key={props.stateSpecialties[i].specialty}>
          <Table.Cell>{props.stateSpecialties[i].specialty}</Table.Cell>
          <Table.Cell>{props.stateSpecialties[i].count}</Table.Cell>
        </Table.Row>
      )
     }
   }
  return (
    <Container>
      <Header as='h2'>Health Service Specialties - {props.state}</Header>
      <Table celled>
        <Table.Header>
          <Table.Row>
            <Table.HeaderCell>Specialty</Table.HeaderCell>
            <Table.HeaderCell>Physician Count</Table.HeaderCell>
          </Table.Row>
        </Table.Header>
        <Table.Body>
          {list}
        </Table.Body>
      </Table>
    </Container>
  );
}
export default StateSpecialties;