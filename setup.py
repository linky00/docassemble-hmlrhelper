import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.hmlrhelper',
      version='0.0.1',
      description=('A docassemble extension that allows you to submit HM Land Registry (HMLR) forms to DocuSign/'),
      long_description='# docassemble.hmlrhelper (beta)\r\n\r\nA docassemble extension that allows you to submit [HM Land Registry (HMLR) forms](https://www.gov.uk/topic/land-registration/searches-fees-forms) to [DocuSign](https://www.docusign.com) through the [DocuSign API](https://developers.docusign.com/) from inside Docassemble interviews.\r\n\r\nThis extension makes use of the awesome [docassemble.docusign](https://pypi.org/project/docassemble.docusign/) \r\nextension created by the lovely people at [Radiant Law](https://radiantlaw.com/).\r\n\r\n## Current limitations\r\n\r\nThis implementation is currently limited to TR1\'s, and is intended to meet the \r\nrequirements for electronic signatures as set out in the *13.3 Our Requirements* section \r\nof [Practice guide 8: execution of deeds ](https://www.gov.uk/government/publications/execution-of-deeds/practice-guide-8-execution-of-deeds#our-requirements).\r\n\r\n* Works for person to person transfers only. There are different requirements and wording \r\nif the transfer is being signed by an attorney or company, or at the direction of the transferor.\r\n* HMLR will accept up to four transferees listed on the TR1 ([see guidance](https://www.gov.uk/government/publications/registered-titles-whole-transfer-tr1/guidance-completing-form-tr1-for-the-transfer-of-registered-property)) however:\r\n    * the size of Box 12 (Execution) on the sample TR1 that this interview populates means there is a \r\n    practical limitation of a maximum of 4 signatories and their and associated witnesses (counting both transferors \r\n    and transferees and noting that transferres don\'t always need to sign).\r\n    * A simple way to improve on this would be the use of a template file where Box 12 (Execution) was extended to use \r\n    the full space available on page three.\r\n* Similarly, addresses are limited to 60 characters in order to fit onto a single line, so you may need to get creative with choosing which address elements are important!    \r\n* The conveyancer still needs to date the deed at the end of the process and submit it to HMLR \'manually\'. \r\n\r\n## Installation & Prerequisites\r\n\r\n1. Install [docassemble.docusign](https://pypi.org/project/docassemble.docusign/) first. Follow the setup and testing process within *docassemble.docusign* to ensure that you can push documents into DocuSign for signature successfully.\r\n\r\n1. Install this docassemble.hmlrhelper package from within your Docassemble package management screen using the latest stable verison available in PyPi:\r\n\r\n    - [docassemble.hmlrhelper on PyPi](#)\r\n\r\n## Github Repository\r\n    \r\n**Note:** Only install from the Github Repository if you want to input into the development of the extension: \r\n    \r\n- [https://github.com/mattpennington/docassemble-hmlrhelper](https://github.com/mattpennington/docassemble-hmlrhelper)\r\n\r\n\r\n## Configuration & Testing\r\n\r\nAfter you\'ve tested *docassemble.docusign* above, and with the extension still in \r\ntest mode (`test-mode: True`) run the test interview at:\r\n\r\n{YOUR SERVER BASE URL}/interview?i=docassemble.hmlrhelper:data/questions/test.yml.\r\n\r\n1. The interview will allow you to push a sample populated TR1 into DocuSign and run through a working demo of the signatory process.\r\n1. The DocuSign sandbox will send all emails to the the email address of the DocuSign sandbox user you created when setting up *docassemble.docusign*\r\n1. The test interview asks for a mobile phone number that will be used for all SMS\'s for the Two Factor Authentication. Please use your own mobile number! :-)\r\n\r\n## Interview Process within Docassemble\r\n\r\n1. something...\r\n1. Document is pushed to Docusign and workflow completed in Docassemble\r\n\r\n## Process within Docusign\r\n\r\n1. 1st **Transferor** clicks document link in email\r\n1. 1st **Transferor** completes Two Factor Authentication by SMS to access document\r\n1. 1st **Transferor** signs deed\r\n1. 1st **Transferor Witness** clicks document link in email\r\n1. 1st **Transferor Witness** completes Two Factor Authentication by SMS to access document\r\n1. 1st **Transferor Witness** witnesses 1st **Transferor** signature and signs deed\r\n1. (Repeat for all transferors)\r\n1. If **Transferees** need to sign too...\r\n    1. 1st **Transferee** clicks document link in email\r\n    1. 1st **Transferee** completes Two Factor Authentication by SMS to access document\r\n    1. 1st **Transferee** signs deed\r\n    1. 1st **Transferee Witness** clicks document link in email\r\n    1. 1st **Transferee Witness** completes Two Factor Authentication by SMS to access document\r\n    1. 1st **Transferee Witness** witnesses 1st **Transferee** signature and signs deed\r\n    1. (Repeat for all transferees)\r\n1. The conveyancer is asked to review and approve the document\r\n\r\n## Going Live\r\n\r\nIn order to put this interview live, you will need to set test mode to false (`test-mode: False`)\r\nin your the configuration for *docassemble.docusign*. You may also need to follow the steps to move \r\nyour application out of the Sandbox and into Docusign\'s live environment if you haven\'t done this \r\nfor other documents submitted using *docassemble.docusign* already. Check out the *docassemble.docusign*\r\ndocumentation to find out how to do this.\r\n\r\n## Future Possible Improvements\r\n\r\n* Using the HMLR API to lookup the property address/reference, though arguably the conveyancer should have these details to hand anyway \r\nso perhaps keying them in saves possible lookup errors at this stage. Equally pulling the data from a case management \r\nsystem would be great too.\r\n* allow the buyer/seller to add their own witness details and invite them when the document \r\nreaches them and before they undertake the signing.\r\n* Whilst this implementation of the helper uses Docusign\'s SMS functionality for Recipient Identity Authentication, its worth noting that Phone Authentication could be made available too for signatories/witnesses that are unable to receive SMS.\r\n* Docusign also supports Knowledge-Based Authentication (KBA) which might prove useful in future.\r\n* HMLR are looking to a future beyond Witnessed electronic signatures to [Qualified electronic signatures](https://www.gov.uk/government/news/hm-land-registry-to-accept-electronic-signatures), therefore further extension through Docusign may be needed in future.\r\n* The implementation uses Signer Recipients rather than Witness Recipients in Docusign for the witness signatures \r\nas (at the time this version was published) *docassemble.docusign* doesn\'t have support for [Witness Recipients](https://developers.docusign.com/esign-rest-api/reference/Envelopes/EnvelopeRecipients/#witness-recipient)\r\n\r\n## Disclaimer\r\n\r\nThis is a beta version and as such may contain bugs/unexpected output.\r\n\r\n## Software License & Copyright Notice\r\n\r\nCopyright (c) 2020 Matt Pennington - Tonic Workflows\r\n\r\nPermission is hereby granted, free of charge, to any person obtaining a copy\r\nof this software and associated documentation files (the "Software"), to deal\r\nin the Software without restriction, including without limitation the rights\r\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\r\ncopies of the Software, and to permit persons to whom the Software is\r\nfurnished to do so, subject to the following conditions:\r\n\r\nThe above copyright notice and this permission notice shall be included in all\r\ncopies or substantial portions of the Software.\r\n\r\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\r\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\r\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\r\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\r\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\r\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\r\nSOFTWARE.\r\n\r\n## TR1 Copyright Notice\r\n\r\nThe *Transfer of whole of registered titles (TR1)* form is (c) Crown copyright (ref: LR/HO).',
      long_description_content_type='text/markdown',
      author='Matt Pennington',
      author_email='mp@tonic.works',
      license='The MIT License (MIT)',
      url='https://tonic.works',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/hmlrhelper/', package='docassemble.hmlrhelper'),
     )

