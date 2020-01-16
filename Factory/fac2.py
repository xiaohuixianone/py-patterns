from abc import ABCMeta,abstractmethod


class Section(metaclass=ABCMeta):

    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print("Person Section")


class AlbumSection(Section):
    def describe(self):
        print("Album Section")

class PatentSetion(Section):
    def describe(self):
        print("Patent Section")

class PublicationSection(Section):
    def describe(self):
        print("Public Section")




class Profile(metaclass=ABCMeta):

    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self,section):
        self.sections.append(section)


class Zhihu(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())
        self.addSections(PublicationSection())


class Csdn(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSetion())

if __name__ == '__main__':
    profile_type = input("which profile you'd like to create (Zhihu or Csdn)")
    profile = eval(profile_type)()
    print("create profile..", type(profile).__name__)
    print("Profile has sections --", profile.getSections())

