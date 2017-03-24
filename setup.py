import os


def setenv_variable(varname, value):
	"""
	sets environment variable `varname` to `value`
	"""
	os.environ[varname] = value


# Set GOOGLE API CREDENTIALS
setenv_variable('GOOGLE_APPLICATION_CREDENTIALS', '../DeepEduVision-08872d7dd7f4.json')