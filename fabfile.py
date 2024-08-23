from fabric.api import cd, env, local, prefix, run

env.hosts = ['sdelquin.me']


def deploy():
    local('git push')
    with cd('~/code/sysmon'):
        with prefix('source .venv/bin/activate'):
            run('git pull')
            run('pip install -r requirements.txt')
            run('supervisorctl restart sysmon')
