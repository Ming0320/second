p = 'ios/App/App.xcodeproj/project.pbxproj'
s = open(p).read()
s = s.replace('CODE_SIGN_STYLE = Automatic;', 'CODE_SIGN_STYLE = Manual;')
import re
s = re.sub(r'DEVELOPMENT_TEAM = .*;', 'DEVELOPMENT_TEAM = "";', s)
s = re.sub(r'CODE_SIGN_IDENTITY = .*;', 'CODE_SIGN_IDENTITY = "";', s)
s = s + '\nCODE_SIGNING_ALLOWED = NO;\n'
open(p, 'w').write(s)
print('signing patched')
