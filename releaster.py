import argparse
from github import Github
import semver

def formatVersion(version):
    return version.replace('v', '')

__author__ = 'github.com/patHyatt'
parser = argparse.ArgumentParser(description='CLI tool to help identify differences between GitHub releases')
parser.add_argument('-repo', help='GitHub repo you wish to compare releases against', required=True)
parser.add_argument('-current', help='Current version of the library/package you are using', required=True)
parser.add_argument('-proposed', help='Proposed version of the library/package you intend to use', required=True)

args = parser.parse_args()

api = Github()

repository = args.repo
repo = api.get_repo(repository)

version_current = semver.parse_version_info(formatVersion(args.current))
version_proposed = semver.parse_version_info(formatVersion(args.proposed))

if version_current > version_proposed:
    print('versions should be provided in highest to lowest, swapping versions')
    version_current, version_proposed = version_current, version_current

applicable_releases = []
for release in repo.get_releases():
    print(f'evaluating {release.tag_name}')
    try:
        version = semver.parse_version_info(formatVersion(release.tag_name))
    except ValueError as ve:
        print(f'"{release.tag_name}" is not a valid semver string, skipping')
        continue

    if version_current < version and version <= version_proposed:
        applicable_releases.append(release)

    if version < version_current:
        print('exiting, no longer need')
        break #no need to evaluate further

for yay in applicable_releases:
    print('****************************************')
    print(f'Release {yay.title} ({yay.tag_name})')
    print(yay.body)
    print()


