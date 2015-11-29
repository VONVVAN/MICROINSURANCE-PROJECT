from django.test import TestCase
from django.utils import timezone
from microinsurance.models import Branch
import datetime

class MicroInsuranceModelTest(TestCase):
    
    def test_creating_a_new_branch_and_saving_it_to_the_database(self):
        # start by creating a new Poll object with its "question" set
        branch = Branch()
        branch.branch_name = 'Ilocos Branch'
        branch.date_created = timezone.now()

        # check we can save it to the database
        branch.save()

        # now check we can find it in the database again
        all_branches_in_database = Branch.objects.all()
        self.assertEquals(len(all_branches_in_database), 1)
        only_branch_in_database = all_branches_in_database[0]
        self.assertEquals(only_branch_in_database, branch)

        # and check it's saved its two attribute the branch name and date created
        self.assertEquals(only_branch_in_database.branch_name, "Ilocos Branch")
        self.assertEquals(only_branch_in_database.date_created, branch.date_created)
    