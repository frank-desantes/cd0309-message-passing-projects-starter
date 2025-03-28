/**
 * @fileoverview gRPC-Web generated client stub for 
 * @enhanceable
 * @public
 */

// Code generated by protoc-gen-grpc-web. DO NOT EDIT.
// versions:
// 	protoc-gen-grpc-web v1.5.0
// 	protoc              v5.29.3
// source: connections.proto


/* eslint-disable */
// @ts-nocheck



const grpc = {};
grpc.web = require('grpc-web');

const proto = require('./connections_pb.js');

/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?grpc.web.ClientOptions} options
 * @constructor
 * @struct
 * @final
 */
proto.ConnectionServiceClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options.format = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname.replace(/\/+$/, '');

};


/**
 * @param {string} hostname
 * @param {?Object} credentials
 * @param {?grpc.web.ClientOptions} options
 * @constructor
 * @struct
 * @final
 */
proto.ConnectionServicePromiseClient =
    function(hostname, credentials, options) {
  if (!options) options = {};
  options.format = 'text';

  /**
   * @private @const {!grpc.web.GrpcWebClientBase} The client
   */
  this.client_ = new grpc.web.GrpcWebClientBase(options);

  /**
   * @private @const {string} The hostname
   */
  this.hostname_ = hostname.replace(/\/+$/, '');

};


/**
 * @const
 * @type {!grpc.web.MethodDescriptor<
 *   !proto.ConnectionRequest,
 *   !proto.ConnectionResponse>}
 */
const methodDescriptor_ConnectionService_GetConnections = new grpc.web.MethodDescriptor(
  '/ConnectionService/GetConnections',
  grpc.web.MethodType.UNARY,
  proto.ConnectionRequest,
  proto.ConnectionResponse,
  /**
   * @param {!proto.ConnectionRequest} request
   * @return {!Uint8Array}
   */
  function(request) {
    return request.serializeBinary();
  },
  proto.ConnectionResponse.deserializeBinary
);


/**
 * @param {!proto.ConnectionRequest} request The
 *     request proto
 * @param {?Object<string, string>} metadata User defined
 *     call metadata
 * @param {function(?grpc.web.RpcError, ?proto.ConnectionResponse)}
 *     callback The callback function(error, response)
 * @return {!grpc.web.ClientReadableStream<!proto.ConnectionResponse>|undefined}
 *     The XHR Node Readable Stream
 */
proto.ConnectionServiceClient.prototype.getConnections =
    function(request, metadata, callback) {
  return this.client_.rpcCall(this.hostname_ +
      '/ConnectionService/GetConnections',
      request,
      metadata || {},
      methodDescriptor_ConnectionService_GetConnections,
      callback);
};


/**
 * @param {!proto.ConnectionRequest} request The
 *     request proto
 * @param {?Object<string, string>=} metadata User defined
 *     call metadata
 * @return {!Promise<!proto.ConnectionResponse>}
 *     Promise that resolves to the response
 */
proto.ConnectionServicePromiseClient.prototype.getConnections =
    function(request, metadata) {
  return this.client_.unaryCall(this.hostname_ +
      '/ConnectionService/GetConnections',
      request,
      metadata || {},
      methodDescriptor_ConnectionService_GetConnections);
};


module.exports = proto;

