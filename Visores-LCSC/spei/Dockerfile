# @name Chunk
# @title
# @version 1.0.0
# @license GPL version 3 or newer
#
# @author
# Fergus Reig-Gracia <http://fergusreig.es>; Environmental Hydrology, Climate and Human Activity Interactions, Geoenvironmental Processes, IPE, CSIC <https://www.ipe.csic.es/hidrologia-ambiental>
#
# @description
# From a netCDF file, generate two versions with the same data but with different chunk
# configurations. In one case, favor the retrieval of temporal series of the main
# variable in each pixel, and in the other, favor the retrieval of planes for each date.

#####################################################################
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/> <http://www.gnu.org/licenses/gpl.txt/>.
#####################################################################

ARG DEBIAN_FRONTEND=noninteractive
ARG DEBCONF_NONINTERACTIVE_SEEN=true
FROM debian:latest
WORKDIR /
SHELL ["/bin/bash", "--login", "-c"]
RUN apt-get update
RUN apt-get install -y python3 
RUN apt-get install -y python3.13-venv
RUN apt-get install -y git
RUN mkdir /root/Downloads/
