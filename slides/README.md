# Lessons from the Trenches: rewriting and re-releasing virtualenv

[Talk for EuroPython 2020 - Online](https://ep2020.europython.eu/talks/D2SG8Vb-lessons-from-the-trenches-rewriting-and-re-releasing-virtualenv/).

## Abstract

virtualenv is a tool that builds virtual environments for Python. It was first created in September 2007 and lived most
of its life being a single file project with an increasing amount of (scary) workarounds within. It managed to grow
until it was 2,700 lines of code. Maintaining this project became increasingly more troublesome, to the point where, we
had more than 500 open issues at one point. In July 2019, I started working from scratch on a rewrite, with the goal of
not just increasing the project's maintainability, but also to make it faster and add some new features that were just
impossible or too hard to do in the existing code base. Fast forward six months to January 2020, when we released the
first beta, with the first full release coming out on 10th February. It took a bit more than a month to squash all the
open bugs tickets, but April started without any remaining open bug tickets. This talk will cover the lessons I've
learned while on this journey.
