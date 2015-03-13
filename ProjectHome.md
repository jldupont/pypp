This project consists of a PYthon PreProcessor.

# Features #
  * Ease of use: just one import statement
  * Speed: once compilation is done, no runtime overhead
  * Based on the [Mako template engine](http://www.makotemplates.org/)
  * Open & close tags can be preceded with # comment character
  * No special file to define (as opposed to [MetaPython](http://code.google.com/p/metapython/))

# Usage #
Just insert the following import statement in your project:
```
 import pypp
```
At the point where the import is done (ie. from an interpreter executing your project's code point of view), any module file with the following directive:
```
 #.pypp
```
will be _preprocessed_ through the template engine and a resulting module file (with the added extension _.pypp_) will be created and loaded in the interpreter.

## Mako Tags ##
Mako tags such as **include** and **def** can be preceded by a python hash # comment character in order to better integrate with source code editors such as Eclipse. Example:
```
 #<%include file="some-file-name" />
 #<%def name="some-variable-name()">some-variable-value</%def>
```
The comment # hash characters will be removed prior to preprocessing; so, the equivalent template code passed to the Mako preprocessor will be:
```
 <%include file="some-file-name" />
 <%def name="some-variable-name()">some-variable-value</%def>
```

# Examples #
Look under http://code.google.com/p/pypp/source/browse/#svn/trunk/tests for some examples.

# Installation #
The package can be installed with _easy\_install_ :

```
 easy_install pypp
```