from fabric.api import env, local, cd, run, prefix

env.hosts = ['cloud']


def deploy():
    local('git push')
    with prefix('source ~/.virtualenvs/sysmon/bin/activate'):
        with cd('~/code/sysmon'):
            run('git pull')
            run('pip install -r requirements.txt')
            run('supervisorctl restart sysmon')
