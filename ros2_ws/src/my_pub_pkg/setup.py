from setuptools import find_packages, setup

package_name = 'my_pub_pkg'

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
    maintainer='nath',
    maintainer_email='nath@todo.todo',
    description='Mi primer publicador y suscriptor en ROS2',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={  # 👈 SOLO UNA VEZ AQUÍ
        'console_scripts': [
            'publicador = my_pub_pkg.publicador:main',
            'suscriptor = my_pub_pkg.suscriptor:main',
        ],
    },
)
