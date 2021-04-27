# Packaging tutorial - PyCon US 2021

For most developers, Python packaging feels like a magical (and cryptic) black box. Apps and libraries use a variety of
tools and have different packaging challenges. Once you start reading up on this topic, you come across many seemingly
random components: `setuptools`, `pip`, `poetry`, `wheels`, `pyproject.toml`, `MANIFEST.in`, virtual environments,
`zippapp`, `shiv`, `pex`, and so on. The sheer number of concepts to master can be overwhelming, leading many
programmers to conclude that packaging in Python is a mess. Before you despair, join me in this tutorial session where
you'll have a chance to learn how to package and publish/deploy your library and/or application through hands-on
exercises.

## Topics

- How and why library packaging differs from application packaging?
- Differences between a source tree/source distribution/wheel.
- Differences between a build back-end and a build front-end (and why we even have this separation).
- Tools used for packaging your library.
- Tools and techniques used to package your application.
- Testing your package for correctness.

## Tutorial outline

1. Introduction

   1. about me + python packaging is a hard subject, but we'll shed some light on it (PyPa only)
   2. Demo problem - Calculating pi 3. How to share code? (we can as library or as an app)

2. The library case

   1. Sharing code as a library, means that we can import and use it in a python interpreter/environment
   2. Understand python interpreter environments -> virtual environments
   3. Understand python import system
   4. Sharing a code is making available the code in the `purelib`/`platlib` folders, so that the importer can load it

      1. Developer source tree
      2. Package builder
      3. Package uploader
      4. Package downloader
      5. Package installer into a python environment

   5. Package types
      1. Sdist - build a wheel - developer tree minus project management file
      2. Wheel - binary -> extract + generate entry points + meta files - files needed at runtime
   6. Package builder -> backend + frontend
      1. Package backend - PEP-517 (flit + setuptools + poetry) -> package dependencies (sdist/wheel)
         1. flit - `pyproject.toml` based show off
         2. setuptools (distutils) - do this as a hands-on code - `setup.py` + `setup.cfg` + `manifest.in`
         3. poetry - `pyproject.toml` based d. scons + etc 2. Package frontend (build/pip/poetry) -> create isolated
            build environment, translate user input to PEP-517 commands
   7. Why do we need sdist when we have wheels? - speed - c-extension allows using platform specific optimizations, but
      we don't know all the target platforms ahead (also sometimes used for auditing - enterprise environments) Example
      cython version of pi approximation (measure the code) Hands-on packaging.
   8. Package uploader -> twine/poetry/copy/email
   9. Package downloader + installer -> pip, though install project available soon; package dependencies can be loaded
      at install time, latest compatible

3. The application case
   1. Sharing code as an application means the target machine is able to run the exposed entry point
   2. Important to run with the same python + dependencies -> requirements.txt file
   3. zipapp
      1. the app only zipped
      2. the dependencies also zipped - virtualenv magic
   4. shiv/pex
   5. pyinstaller - make a single executable
