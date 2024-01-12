# Generated by IBM TransformationAdvisor
# Wed May 05 19:05:52 UTC 2021

FROM ibmcom/websphere-traditional:8.5.5.22-ubi8

# put app and scripts and properties in /work/config
# put external library (e.g db driver) in /work/config/lib
COPY --chown=was:root defaultapplication.war /work/config/defaultapplication.war
COPY --chown=was:root ./src/config /work/config
COPY --chown=was:root ./lib /work/config/lib
RUN /work/configure.sh
