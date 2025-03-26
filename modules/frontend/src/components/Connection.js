import React, { Component } from "react";
import { ConnectionServiceClient } from './connections_grpc_web_pb';
import { ConnectionRequest } from './connections_pb';

class Connection extends Component {
  constructor(props) {
    super(props);

    this.state = {
      connections: [],
      personId: null,
    };
  }

  componentDidUpdate() {
    const { personId } = this.props;
    if (Number(personId) !== Number(this.state.personId)) {
      this.setState({ personId, connections: this.state.connections });
      this.getConnections(personId);
    }
  }

  // getConnections = (personId) => {
  //   if (personId) {
  //     // TODO: endpoint should be abstracted into a config variable
  //     fetch(
  //       `http://localhost:30001/api/persons/${personId}/connection?start_date=2020-01-01&end_date=2020-12-30&distance=5`
  //     )
  //       .then((response) => response.json())
  //       .then((connections) =>
  //         this.setState({
  //           connections: connections,
  //           personId: this.state.personId,
  //         })
  //       );
  //   }
  // };

  getConnections = (personId) => {
    console.log('enter getConnections');

    //const client = new ConnectionServiceClient('http://udaconnect_grpc_api:5003');
    const client = new ConnectionServiceClient('http://localhost:30003');

    console.log(client);

    if (personId) {
      const request = new ConnectionRequest();
      request.setPersonId(personId);
      request.setStartDate('2020-01-01');
      request.setEndDate('2020-12-30');
      request.setDistance(5);

      client.getConnections(request, {}, (err, response) => {
        if (err) {
          console.error(err);
          return;
        }
        const connections = response.getConnectionsList();
        this.setState({
          connections: connections,
          personId: this.state.personId,
        });
      });
    }
  };

  render() {
    return (
      <div className="connectionBox">
        <div className="connectionHeader">Connections</div>
        <ul className="connectionList">
          {this.state.connections.filter((value, index, a) => a.findIndex(v => (
            v.person.id === value.person.id
          )) === index).map((connection, index) => (
            <li className="connectionListItem" key={index}>
              <div className="contact">
                {connection.person.first_name} {connection.person.last_name}
              </div>
              <div>
                met at
                <span className="latlng">
                  {` `}
                  {connection.location.latitude},{` `}
                  {connection.location.longitude}
                </span>
                <br />
                {`on `}
                {new Date(connection.location.creation_time).toDateString()}
              </div>
            </li>
          ))}
        </ul>
      </div>
    );
  }
}
export default Connection;
