from setuptools import setup

package_name = 'grobot_aruco'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jung Woo Hyeon',
    maintainer_email='jungwoohyeon@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'aruco_node = ros2_aruco.aruco_node:main',
            'aruco_check = ros2_aruco.aruco_check:main'
        ],
    },
)
