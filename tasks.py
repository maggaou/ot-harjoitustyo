from sys import platform
from invoke import task

@task
def database(ctx):
    ctx.run("python src/initialize_database.py", pty=True)

@task
def build(ctx):
    ctx.run("python src/build.py")

@task
def start(ctx):
    print("Nothing to run yet")

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task(test)
def test_and_report(ctx):
    ctx.run("coverage html", pty=True)
    file = "htmlcov/index.html"
    if platform == "darwin":
        print("macOS test report " + file)
    if platform == "linux":
        print("linux test report " + file)
