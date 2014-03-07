from fabric.api import local, lcd

def prepare_deployment(branch_name):
    branch_name = 'basics'
    local('python manage.py test booked_site')
    local('git add -p && git commit')
    local('git checkout master && git merge ' + branch_name)

def deploy():
    with lcd('/home/tom/mysite')
        local('git pull /home/tom/dev/mysite')
        local('python manage.py migrate booked_site')
        local('python manage.py test booked_site')
        local('django_admin.py runserver &')


def pycrm():
    local("find . -name '*.pyc' -delete")
