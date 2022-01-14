import imp


import os
import subprocess
import unittest

class IcdCodeConverterTests(unittest.TestCase):

    def setUp(self) -> None:
        self.command_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "icd_code_converter")
        subprocess.Popen([self.command_path, "-h"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()

    def test_convert_icd9(self) -> None:
        icd9_code = "401.9"

        ps = subprocess.Popen([self.command_path, "--icd9", icd9_code], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = ps.communicate()[0].decode()
        
        self.assertTrue(isinstance(output, str))
        self.assertEqual(["I10", "I169"], output.split(","))
    
    def test_convert_icd9_no_mapping(self) -> None:
        invalid_code = "401.99999"

        ps = subprocess.Popen([self.command_path, "--icd9", invalid_code], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = ps.communicate()[0].decode()
        
        self.assertTrue(isinstance(output, str))
        self.assertEqual(["NA"], output.split(","))
    
    def test_convert_icd10(self) -> None:
        icd10_code = "I10"

        ps = subprocess.Popen([self.command_path, "--icd10", icd10_code], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = ps.communicate()[0].decode()
        
        self.assertTrue(isinstance(output, str))
        self.assertEqual(['4010', '4011', '4019'], output.split(","))
    
    def test_convert_icd10_no_mapping(self) -> None:
        invalid_code = "I100000000"

        ps = subprocess.Popen([self.command_path, "--icd10", invalid_code], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = ps.communicate()[0].decode()
        
        self.assertTrue(isinstance(output, str))
        self.assertEqual(["NA"], output.split(","))
