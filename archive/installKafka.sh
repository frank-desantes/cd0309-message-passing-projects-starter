#!/bin/bash
helm uninstall my-kafka -n kafka
helm install my-kafka oci://registry-1.docker.io/bitnamicharts/kafka -n kafka -f values.yaml
