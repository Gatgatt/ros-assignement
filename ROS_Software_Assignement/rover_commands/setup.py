from setuptools import find_packages, setup

package_name = 'rover_commands'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='xplore',
    maintainer_email='xplore@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
           'gamepad = rover_commands.gamepad:main',
           'subscriber = rover_commands.subscriber:main',
           'sensor = rover_commands.sensor:main',
           'gps = rover_commands.gps:main',
            'process = rover_commands.process:main'
        ],
    },
)
