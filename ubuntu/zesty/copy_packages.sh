#!/bin/bash

DISTRO="$1"
PKGEXT="$2"

mkdir -p /packages/${DISTRO} && echo "created /packages/${DISTRO}" || echo "failed to create created /packages/${DISTRO}"

if [ -d "/packages/${DISTRO}" ]
then
  mv $DISTRO_DIR/*.${PKGEXT} /packages/${DISTRO} && echo "moved *.${PKGEXT} to /packages/${DISTRO}" || echo "failed to move *.${PKGEXT} to /packages/${DISTRO}"
fi