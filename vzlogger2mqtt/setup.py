from setuptools import setup

setup(name='vzlogger2mqtt',
      version='0.2',
      description='vzlogger 2 MQTT bridge',
      url='https://github.com/gbeine/vzlogger2mqtt',
      author='Gerrit',
      author_email='mail@gerritbeine.de',
      license='MIT',
      packages=['vzlogger2mqtt'],
      requires=[
          'logging',
          'paho.mqtt',
          'pyyaml',
        ],
      zip_safe=False)
