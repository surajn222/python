# https://pythonwife.com/proxy-design-pattern-with-python/

class PatientDataManager:
	""" Real Subject"""

	def __init__(self):
		self.__patients = {}

	def _add_patient(self, patient_id, data):
		self.__patients[patient_id] = data

	def _get_patient(self, patient_id):
		Problem, Date = self.__patients[patient_id]
		return f"Name: {patient_id}, Problem: {Problem}, Date: {Date}"


class AccessPatientData(PatientDataManager):
	""" Proxy Subject"""

	def __init__(self, fm):
		self.fm = fm

	def add_patient(self, patient_id, data, password):
		if password == '1234':
			self.fm._add_patient(patient_id, data)
		else:
			print("Wrong password.")

	def get_patient(self, patient_id, password):
		if password == '1234':
			return self.fm._get_patient(patient_id)
		else:
			print("Unauthorized Access.")

obj = AccessPatientData(PatientDataManager())
obj.add_patient('Vinayak', ['pneumonia', '2021-11-09'], '1234')

print(obj.get_patient('Vinayak', '1234'))