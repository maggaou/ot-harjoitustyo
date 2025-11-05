from sys import platform
from invoke import task

@task
def start(ctx):
    print("Nothing to run yet")

@task
def test(ctx):
    print("Nothing to test yet")
    ctx.run("coverage --help", pty=True)

@task(test)
def test_and_report(ctx):
    ctx.run("coverage html", pty=True)
    file = "htmlcov/index.html"
    if platform == "darwin":
        print("macOS test report " + file)
    if platform == "linux":
        print("linux test report " + file)