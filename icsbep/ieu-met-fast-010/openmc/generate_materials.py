import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Empty matrix above and below reflector"
mat.set_density('sum')
mat.add_element('Cr', 1.18909e-3)
mat.add_element('Ni', 4.80175e-4)
mat.add_element('Fe', 4.27914e-3)
mat.add_element('C', 1.87415e-5)
mat.add_element('Mo', 8.25653e-6)
mat.add_element('Mn', 1.05905e-4)
mat.add_element('Cu', 1.72319e-5)
mat.add_element('Si', 6.83105e-5)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Empty matrix surrounding radial reflector"
mat.set_density('sum')
mat.add_element('Cr', 1.17957e-3)
mat.add_element('Ni', 4.76329e-4)
mat.add_element('Fe', 4.24488e-3)
mat.add_element('C', 1.85933e-5)
mat.add_element('Mo', 8.19076e-6)
mat.add_element('Mn', 1.05057e-4)
mat.add_element('Cu', 1.70944e-5)
mat.add_element('Si', 6.77630e-5)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "DU radial reflector"
mat.set_density('sum')
mat.add_nuclide('U235', 8.56868e-5)
mat.add_nuclide('U238', 3.83747e-2)
mat.add_element('Cr', 1.69502e-3)
mat.add_element('Ni', 6.86302e-4)
mat.add_element('Fe', 6.13244e-3)
mat.add_element('C', 3.77935e-5)
mat.add_element('Mo', 1.07671e-5)
mat.add_element('Mn', 1.46803e-4)
mat.add_element('Cu', 2.16820e-5)
mat.add_element('H', 2.53803e-6)
mat.add_element('Si', 7.69676e-5)
mat.add_element('Cl', 4.39454e-6)
mat.add_element('F', 1.30132e-5)
mats.append(mat)

mat = openmc.Material(4)
mat.name = "Lower DU axial reflector"
mat.set_density('sum')
mat.add_nuclide('U235', 8.24312e-5)
mat.add_nuclide('U238', 3.69113e-2)
mat.add_element('Cr', 1.72627e-3)
mat.add_element('Ni', 7.03836e-4)
mat.add_element('Fe', 6.26607e-3)
mat.add_element('Al', 4.16747e-4)
mat.add_element('C', 3.97675e-5)
mat.add_element('Mo', 1.12206e-5)
mat.add_element('Mn', 1.46859e-4)
mat.add_element('Cu', 2.13537e-5)
mat.add_element('H', 2.81777e-6)
mat.add_element('Si', 8.31237e-5)
mat.add_element('Cl', 4.87118e-6)
mat.add_element('F', 1.44249e-5)
mats.append(mat)

mat = openmc.Material(5)
mat.name = "Upper DU axial reflector"
mat.set_density('sum')
mat.add_nuclide('U235', 8.31425e-5)
mat.add_nuclide('U238', 3.72293e-2)
mat.add_element('Cr', 1.72627e-3)
mat.add_element('Ni', 7.03836e-4)
mat.add_element('Fe', 6.26656e-3)
mat.add_element('Al', 4.16747e-4)
mat.add_element('C', 3.99149e-5)
mat.add_element('Mo', 1.12206e-5)
mat.add_element('Mn', 1.46859e-4)
mat.add_element('Cu', 2.13537e-5)
mat.add_element('H', 2.85427e-6)
mat.add_element('Si', 8.31237e-5)
mat.add_element('Cl', 4.93394e-6)
mat.add_element('F', 1.46107e-5)
mats.append(mat)

mat = openmc.Material(6)
mat.name = "Core 1"
mat.set_density('sum')
mat.add_nuclide('U235', 3.48543e-3)
mat.add_nuclide('U238', 3.52634e-2)
mat.add_nuclide('U234', 3.34211e-5)
mat.add_nuclide('U236', 1.60227e-5)
mat.add_element('Cr', 1.86067e-3)
mat.add_element('Ni', 7.49053e-4)
mat.add_element('Fe', 6.65688e-3)
mat.add_element('C', 9.62990e-5)
mat.add_element('Mo', 1.18327e-5)
mat.add_element('Mn', 1.63509e-4)
mat.add_element('Cu', 2.38833e-5)
mat.add_element('H', 1.94580e-5)
mat.add_element('Si', 7.16001e-5)
mat.add_element('Cl', 3.33506e-5)
mat.add_element('F', 9.91220e-5)
mats.append(mat)

mat = openmc.Material(7)
mat.name = "Core 2"
mat.set_density('sum')
mat.add_nuclide('U235', 3.47666e-3)
mat.add_nuclide('U238', 3.53869e-2)
mat.add_nuclide('U234', 3.33328e-5)
mat.add_nuclide('U236', 1.59801e-5)
mat.add_element('Cr', 1.87418e-3)
mat.add_element('Ni', 7.54654e-4)
mat.add_element('Fe', 6.70752e-3)
mat.add_element('C', 9.64166e-5)
mat.add_element('Mo', 1.19799e-5)
mat.add_element('Mn', 1.64823e-4)
mat.add_element('Cu', 2.42329e-5)
mat.add_element('H', 1.94498e-5)
mat.add_element('Si', 7.42038e-5)
mat.add_element('Cl', 3.34686e-5)
mat.add_element('F', 9.94726e-5)
mats.append(mat)

mat = openmc.Material(8)
mat.name = "Core 3"
mat.set_density('sum')
mat.add_nuclide('U235', 3.48543e-3)
mat.add_nuclide('U238', 3.52634e-2)
mat.add_nuclide('U234', 3.34211e-5)
mat.add_nuclide('U236', 1.60227e-5)
mat.add_element('Cr', 1.86067e-3)
mat.add_element('Ni', 7.49053e-4)
mat.add_element('Fe', 6.65688e-3)
mat.add_element('C', 9.62606e-5)
mat.add_element('Mo', 1.18327e-5)
mat.add_element('Mn', 1.63509e-4)
mat.add_element('Cu', 2.38833e-5)
mat.add_element('H', 1.94471e-5)
mat.add_element('Si', 7.16001e-5)
mat.add_element('Cl', 3.33314e-5)
mat.add_element('F', 9.90650e-5)
mats.append(mat)

mat = openmc.Material(9)
mat.name = "Core 4"
mat.set_density('sum')
mat.add_nuclide('U235', 3.47666e-3)
mat.add_nuclide('U238', 3.53869e-2)
mat.add_nuclide('U234', 3.33328e-5)
mat.add_nuclide('U236', 1.59801e-5)
mat.add_element('Cr', 1.87418e-3)
mat.add_element('Ni', 7.54654e-4)
mat.add_element('Fe', 6.70752e-3)
mat.add_element('C', 9.63781e-5)
mat.add_element('Mo', 1.19799e-5)
mat.add_element('Mn', 1.64823e-4)
mat.add_element('Cu', 2.42329e-5)
mat.add_element('H', 1.94388e-5)
mat.add_element('Si', 7.42038e-5)
mat.add_element('Cl', 3.34493e-5)
mat.add_element('F', 9.94154e-5)
mats.append(mat)

mats.export_to_xml()