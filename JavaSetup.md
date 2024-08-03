# Java Setup: 
Here are the commands to install each JAR file to your local Maven repository. Assuming you are already in the `lib` directory:

```sh
mvn install:install-file -Dfile=Spex-1.1.jar -DgroupId=org.processmining -DartifactId=spex -Dversion=1.1 -Dpackaging=jar

mvn install:install-file -Dfile=UITopiaResources-0.6-20190913.jar -DgroupId=org.processmining -DartifactId=uitopia-resources -Dversion=0.6 -Dpackaging=jar

mvn install:install-file -Dfile=Uitopia-0.6-20190913.jar -DgroupId=org.processmining -DartifactId=uitopia -Dversion=0.6 -Dpackaging=jar

mvn install:install-file -Dfile=bsh-2.0b4.jar -DgroupId=bsh -DartifactId=bsh -Dversion=2.0b4 -Dpackaging=jar

mvn install:install-file -Dfile=commons-compress-1.13.jar -DgroupId=org.apache.commons -DartifactId=commons-compress -Dversion=1.13 -Dpackaging=jar

mvn install:install-file -Dfile=commons-logging-1.1.3.jar -DgroupId=commons-logging -DartifactId=commons-logging -Dversion=1.1.3 -Dpackaging=jar

mvn install:install-file -Dfile=guava-16.0.1.jar -DgroupId=com.google.guava -DartifactId=guava -Dversion=16.0.1 -Dpackaging=jar

mvn install:install-file -Dfile=jargs-latest.jar -DgroupId=jargs -DartifactId=jargs -Dversion=latest -Dpackaging=jar

mvn install:install-file -Dfile=jgraph-5.13.0.4.jar -DgroupId=jgraph -DartifactId=jgraph -Dversion=5.13.0.4 -Dpackaging=jar

mvn install:install-file -Dfile=junit-4.12.jar -DgroupId=junit -DartifactId=junit -Dversion=4.12 -Dpackaging=jar

mvn install:install-file -Dfile=slickerbox-1.0rc1.jar -DgroupId=slickerbox -DartifactId=slickerbox -Dversion=1.0rc1 -Dpackaging=jar

mvn install:install-file -Dfile=OpenXES-20211004.jar -DgroupId=org.deckfour -DartifactId=openxes -Dversion=20211004 -Dpackaging=jar

mvn install:install-file -Dfile=ProM-Framework.jar -DgroupId=org.processmining -DartifactId=prom-framework -Dversion=6.13 -Dpackaging=jar

mvn install:install-file -Dfile=ProM-Contexts.jar -DgroupId=org.processmining -DartifactId=prom-contexts -Dversion=6.13 -Dpackaging=jar

mvn install:install-file -Dfile=ProM-Models.jar -DgroupId=org.processmining -DartifactId=prom-models -Dversion=6.13 -Dpackaging=jar

mvn install:install-file -Dfile=ProM-Plugins.jar -DgroupId=org.processmining -DartifactId=prom-plugins -Dversion=6.13 -Dpackaging=jar

mvn install:install-file -Dfile=XESStandard.jar -DgroupId=org.deckfour -DartifactId=xes-standard -Dversion=20211004 -Dpackaging=jar
```

### Update Your POM File

After installing the JAR files locally, include them in your `pom.xml` as dependencies:
