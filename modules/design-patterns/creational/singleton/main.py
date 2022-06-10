class SingletonGovt:
   # This is the single instance that will be used by all objects. We have to return this.
   __instance__ = None

   def __init__(self):
       """ Constructor.
       """
       if SingletonGovt.__instance__ is None:
           SingletonGovt.__instance__ = self
       else:
           raise Exception("You cannot create another SingletonGovt class")

   @staticmethod
   def get_instance():
       """ Static method to fetch the current instance.
       """
       if not SingletonGovt.__instance__:
           SingletonGovt()
       return SingletonGovt.__instance__

government = SingletonGovt()
print(government)

same_government = SingletonGovt.get_instance()
print(same_government)

another_government = SingletonGovt.get_instance()
print(another_government)

new_government = SingletonGovt()
print(new_government)
