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
        
  getConnections = (personId) => {
    if (personId) {
      fetch(
        `http://localhost:30002/api/persons/${personId}/connection?start_date=2020-01-01&end_date=2020-12-30&distance=5`
      )
        .then((response) => response.json())
        .then((connections) =>
          this.setState({
            connections: connections,
            personId: this.state.personId,
          })
        );
    }
  };

        //Quellübergreifende (Cross-Origin) Anfrage blockiert: Die Gleiche-Quelle-Regel verbietet das Lesen der externen Ressource auf http://localhost:30003/ConnectionService/GetConnections. (Grund: CORS-Kopfzeile 'Access-Control-Allow-Origin' fehlt). Statuscode: 200.
        //going with the rest service aboce until mayur can help me on that
  // getConnections = (personId) => {
  //   console.log('enter getConnections');

  //   //const client = new ConnectionServiceClient('http://udaconnect_grpc_api:5003');
  //   const client = new ConnectionServiceClient('http://localhost:30003');

  //   console.log(client);

  //   if (personId) {
  //     const request = new ConnectionRequest();
  //     request.setPersonId(personId);
  //     request.setStartDate('2020-01-01');
  //     request.setEndDate('2020-12-30');
  //     request.setDistance(5);

  //     client.getConnections(request, {}, (err, response) => {
  //       if (err) {
  //         console.error(err);
  //         return;
  //       }
  //       const connections = response.getConnectionsList();
  //       this.setState({
  //         connections: connections,
  //         personId: this.state.personId,
  //       });
  //     });
  //   }
  // };


      //   Starting the development server...
      // Failed to compile.
      // /node_modules/@mapbox/node-pre-gyp/lib/util/s3_setup.js
      // Module not found: Can't resolve 'aws-sdk' in '/node_modules/@mapbox/node-pre-gyp/lib/util'
  // getConnections = (personId) => {
  //   console.log('enter getConnections');
  //   const grpc = require('grpc');
  //   const protoLoader = require('@grpc/proto-loader');

  //   // Load the protobuf
  //   const PROTO_PATH = './connections.proto';
  //   const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  //     keepCase: true,
  //     longs: String,
  //     enums: String,
  //     defaults: true,
  //     oneofs: true
  //   });
  //   const connectionService = grpc.loadPackageDefinition(packageDefinition).ConnectionService;

  //   // Create the client
  //   const client = new connectionService.GetConnections('localhost:50051', grpc.credentials.createInsecure());

  //   console.log(client);

  //   if (personId) {
  //     // Define the request
  //     const request = {
  //       person_id: personId,
  //       start_date: '2025-01-01',
  //       end_date: '2025-12-31',
  //       distance: 5
  //     };
  //     client.getConnections(request, {}, (err, response) => {
  //       if (err) {
  //         console.error(err);
  //         return;
  //       }
  //       const connections = response.getConnectionsList();
  //       this.setState({
  //         connections: connections,
  //         personId: this.state.personId,
  //       });
  //     });
  //   }
  // };


        // /node_modules/@grpc/grpc-js/build/src/server-interceptors.js
        // Module not found: Can't resolve 'http2' in '/node_modules/@grpc/grpc-js/build/src'
  // getConnections = (personId) => {
  //   console.log('enter getConnections');

  //   const grpc = require('@grpc/grpc-js');
  //   const protoLoader = require('@grpc/proto-loader');

  //   // Load the service.proto file
  //   const packageDefinition = protoLoader.loadSync('connections.proto');
  //   const myservice = grpc.loadPackageDefinition(packageDefinition).ConnectionService;

  //   // Create the client
  //   const client = new myservice.GetConnections('http://localhost:30003', grpc.credentials.createInsecure());

  //   console.log(client);

  //   if (personId) {
  //     // Define the request
  //     const request = {
  //       person_id: personId,
  //       start_date: '2025-01-01',
  //       end_date: '2025-12-31',
  //       distance: 5
  //     };

  //     client.getConnections(request, {}, (err, response) => {
  //       if (err) {
  //         console.error(err);
  //         return;
  //       }
  //       const connections = response.getConnectionsList();
  //       this.setState({
  //         connections: connections,
  //         personId: this.state.personId,
  //       });
  //     });
  //   }
  // };

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
