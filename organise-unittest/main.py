import sys
import os
import subprocess
import pandas as pd
import configparser

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
#pd.set_option('display.max_colwidth', -1)
def run_bash_command(command, working_dir = "/tmp"):
    bashCommand = command
    process = subprocess.run(bashCommand.split(), cwd=working_dir, capture_output=True)
    #print(process.stdout)
    #print((process.stderr).strip("\n"))
    output = (process.stdout).decode("utf-8").split("\n")
    error = (process.stderr).decode("utf-8").split("\n")
    print(output)
    print(error)
    return output, error

def clone_gits(list_git_repos, df):
	for repo in list_git_repos:
		run_bash_command("git clone " + str(repo), "repos")

def check_if_tests_folder_present(list_git_repos, df):
	df['tests']='0'
	for repo in list_git_repos:
		print("Repo " + str(repo))
		folder = repo.split("/")[4]
		print(folder)

		for dirpath, dnames, fnames in os.walk("./repos/" + str(folder) + "/"):
			for dirs in dnames:
				if(dirs == "tests"):
					df.loc[df['repos'] == repo, 'tests'] = '1'
					break
			break

	print(df)
	return df


def check_for_file_present(list_git_repos, df):
	df['conftest']='0'
	for repo in list_git_repos:
		folder = repo.split("/")[4]
		print(folder)

		for dirpath, dnames, fnames in os.walk("./repos/" + str(folder) + "/tests/"):
			for file in fnames:
				print("FILE ----- " + str(file))
				if(file == "conftest.py"):
					df.loc[df['repos'] == repo, 'conftest'] = '1'
					break
			break

	print(df)
	return df


def check_for_word_preset_in_files(list_git_repos, df, word):
	df[word]='0'
	for repo in list_git_repos:
		folder = repo.split("/")[4]
		print(folder)

		for dirpath, dnames, fnames in os.walk("./repos/" + str(folder) + "/tests/"):
			for file in fnames:
				print("FILE ----- " + str(file))
				file = "./repos/" + str(folder) + "/tests/" + str(file)
				with open(file, "rb") as f:
					lines = f.readlines()

				for line in lines:
					line = str(line)
					if word in line:
						df.loc[df['repos'] == repo, word] = '1'
						break
			break

	print(df)
	return df


def check_for_word_absent_in_files(list_git_repos, df, word):
	df[word + str("_absent")] = '1'
	for repo in list_git_repos:
		folder = repo.split("/")[4]
		print(folder)

		for dirpath, dnames, fnames in os.walk("./repos/" + str(folder) + "/tests/"):
			for file in fnames:
				print("FILE ----- " + str(file))
				if str(file) != "__init__.py":
					file = "./repos/" + str(folder) + "/tests/" + str(file)
					with open(file, "r", encoding="utf8", errors='ignore') as f:
						lines = f.readlines()

					for line in lines:
						if word in line:
							df.loc[df['repos'] == repo, word + str("_absent")] = '0'
							break
			break

	print(df)
	return df

	pass

def main():
	config = configparser.ConfigParser(allow_no_value=True, delimiters="|")
	config.read('config.ini')
	config.optionxform = str

	# Method 1
	list_git_repos = list(config['repos'])


	df = pd.DataFrame(list_git_repos, columns =['repos'])
	print(df)
	clone_gits(list_git_repos, df)
	df = check_if_tests_folder_present(list_git_repos, df)
	df = check_for_file_present(list_git_repos, df)
	#fixtures
	#pytest
	#unittest
	df = check_for_word_preset_in_files(list_git_repos, df, "fixture")
	df = check_for_word_preset_in_files(list_git_repos, df, "pytest")
	df = check_for_word_preset_in_files(list_git_repos, df, "unittest")



	df  = check_for_word_absent_in_files(list_git_repos, df, "pytest")
	df  = check_for_word_absent_in_files(list_git_repos, df, "unittest")
	#print(df)
	#pytest_df = df["pytest"]=="1"
	pytest_df = df.loc[df['pytest'] == "1"]

	print(pytest_df)

main()

