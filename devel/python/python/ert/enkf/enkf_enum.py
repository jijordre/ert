#  Copyright (C) 2012  Statoil ASA, Norway. 
#   
#  The file 'enkf_enum.py' is part of ERT - Ensemble based Reservoir Tool. 
#   
#  ERT is free software: you can redistribute it and/or modify 
#  it under the terms of the GNU General Public License as published by 
#  the Free Software Foundation, either version 3 of the License, or 
#  (at your option) any later version. 
#   
#  ERT is distributed in the hope that it will be useful, but WITHOUT ANY 
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or 
#  FITNESS FOR A PARTICULAR PURPOSE.   
#   
#  See the GNU General Public License at <http://www.gnu.org/licenses/gpl.html> 
#  for more details. 

from ert.cwrap.cenum import create_enum
from ert.enkf import ENKF_LIB

EnkfStateEnum = create_enum(ENKF_LIB, "enkf_state_enum_iget", "enkf_state_enum")
EnkfRunEnum = create_enum(ENKF_LIB, "enkf_run_enum_iget", "enkf_run_enum")


