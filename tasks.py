# -*- coding: utf-8 -*-
import os
from invoke import task, run

docs_dir = 'docs'
build_dir = os.path.join(docs_dir, '_build')

@task
def test(coverage=False):
    cmd = 'py.test'
    if coverage:
        cmd += ' --cov=webargs --cov-report=term --cov-report=html'
    run(cmd, pty=True)

@task
def clean():
    run("rm -rf build")
    run("rm -rf dist")
    run("rm -rf webargs.egg-info")
    clean_docs()
    print("Cleaned up.")

@task
def readme(browse=False):
    run('rst2html.py README.rst > README.html')
    if browse:
        run('open README.html')

@task
def clean_docs():
    run("rm -rf %s" % build_dir)

@task
def browse_docs():
    run("open %s" % os.path.join(build_dir, 'index.html'))

@task
def docs(clean=False, browse=False):
    if clean:
        clean_docs()
    run("sphinx-build %s %s" % (docs_dir, build_dir), pty=True)
    if browse:
        browse_docs()
