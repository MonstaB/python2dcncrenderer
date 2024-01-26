import re
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D

# File paths
input_file_path = "test2.txt"
output_file_path = "output.txt"

# Variables to store panel size and Z value
panel_size = None
original_z_value = None
current_z_value = None
nulll = "0"

# Variables to store color information
original_color = "darkred"
current_color = "darkred"

# Lists to store legend entries and corresponding colors
legend_entries = []
legend_colors = []

# Lists to store line coordinates and colors
lines_x = []
lines_y = []
lines_colors = []
arcs_radii = []
arcs_directions = []  # 1 for G2 (clockwise), -1 for G3 (counterclockwise)
arcs_colors = []

# Open and read the input file
with open(input_file_path, 'r') as file:
    for line in file:
        # Ignore the line "G0 G90"
        if "G0 G90" in line:
            continue



        # Extract panel size and Z value from the first part of the file
        if line.startswith("G100"):
            values = re.findall(r'[-+]?\d*\.\d+|\d+', line)
            panel_size = (float(values[1]), float(values[2]))
            original_z_value = float(values[3])
            current_z_value = original_z_value

        # Extract material name for title
        elif "(MATERIAL NAME:" in line:
            title = re.search(r'\((MATERIAL NAME:.*?)\)', line).group(1)

        # Extract tool information for legend and color
        elif "(TOOL -" in line:
            tool_info = re.search(r'\((TOOL - .*?)\)', line).group(1)
            legend_entries.append(tool_info)
            legend_colors.append(current_color)

        # Process G0 or G1 lines for color changes and store line coordinates
        elif line.startswith("G0") or line.startswith("G1"):
            values = re.findall(r'[-+]?\d*\.\d+|\d+', line)


            # Check for Z value
            if len(values) == 2:
                current_z_value = float(values[1])

                       # Check if Z value is higher or lower than the original
                if current_z_value > original_z_value:
                    current_color = "lightgrey"
                else:
                    current_color = original_color

            if len(values) == 3:
                if line.startswith("G1 X"):
                    x_value, y_value = float(values[1]), float(values[2])
                    lines_x.append(x_value)
                    lines_y.append(y_value)
                    lines_colors.append(current_color)
                    arcs_radii.append(nulll)
                    arcs_directions.append(nulll)

                else:

                    current_z_value = float(values[1])



                # Check if Z value is higher or lower than the original
                    if current_z_value > original_z_value:
                        current_color = "lightgrey"
                    else:
                        current_color = original_color





            if len(values) == 4:
                if line.startswith("G1 X"):
                    x_value, y_value = float(values[1]), float(values[2])
                    lines_x.append(x_value)
                    lines_y.append(y_value)
                    lines_colors.append(current_color)
                    arcs_radii.append(nulll)
                    arcs_directions.append(nulll)



                else:
                    current_z_value = float(values[3])
                    x_value, y_value = float(values[1]), float(values[2])

                # Check if Z value is higher or lower than the original
                    if current_z_value > original_z_value:
                        current_color = "lightgrey"
                        lines_x.append(x_value)
                        lines_y.append(y_value)
                        lines_colors.append(current_color)
                        arcs_radii.append(nulll)
                        arcs_directions.append(nulll)
                    else:
                        current_color = original_color
                        lines_x.append(x_value)
                        lines_y.append(y_value)
                        lines_colors.append(current_color)
                        arcs_radii.append(nulll)
                        arcs_directions.append(nulll)


            if len(values) == 5:
                current_z_value = float(values[3])
                x_value, y_value = float(values[1]), float(values[2])

                # Check if Z value is higher or lower than the original
                if current_z_value > original_z_value:
                    current_color = "lightgrey"
                    lines_x.append(x_value)
                    lines_y.append(y_value)
                    lines_colors.append(current_color)
                    arcs_radii.append(nulll)
                    arcs_directions.append(nulll)
                else:
                    current_color = original_color
                    lines_x.append(x_value)
                    lines_y.append(y_value)
                    lines_colors.append(current_color)
                    arcs_radii.append(nulll)
                    arcs_directions.append(nulll)


        elif line.startswith("G2") or line.startswith("G3"):
            values = re.findall(r'[-+]?\d*\.\d+|\d+', line)

            if len(values) == 5:
                if "Z" in line:
                    current_z_value = float(values[3])
                    x_value, y_value = float(values[1]), float(values[2])
                    r_value = float(values[4])
                    if line.startswith("G2"):
                        direction = 1  # Clockwise
                    elif line.startswith("G3"):
                        direction = -1  # Counterclockwise

                    if current_z_value > original_z_value:
                        current_color = "lightgrey"
                        lines_x.append(x_value)
                        lines_y.append(y_value)
                        lines_colors.append(current_color)
                        arcs_radii.append(r_value)
                        arcs_directions.append(direction)
                    else:
                        current_color = original_color
                        lines_x.append(x_value)
                        lines_y.append(y_value)
                        lines_colors.append(current_color)
                        arcs_radii.append(r_value)
                        arcs_directions.append(direction)
                else:



                    x_value, y_value = float(values[1]), float(values[2])
                    r_value = float(values[3])
                    if line.startswith("G2"):
                        direction = 1  # Clockwise
                    elif line.startswith("G3"):
                        direction = -1  # Counterclockwise

                    current_color = original_color
                    lines_x.append(x_value)
                    lines_y.append(y_value)
                    lines_colors.append(current_color)
                    arcs_radii.append(r_value)
                    arcs_directions.append(direction)

            if len(values) == 4:
                x_value, y_value = float(values[1]), float(values[2])
                r_value = float(values[3])
                if line.startswith("G2"):
                    direction = 1  # Clockwise
                elif line.startswith("G3"):
                    direction = -1  # Counterclockwise

                current_color = original_color
                lines_x.append(x_value)
                lines_y.append(y_value)
                lines_colors.append(current_color)
                arcs_radii.append(r_value)
                arcs_directions.append(direction)






            # Check for X and Y values
#            if len(values) > 2:
#                x_value, y_value = float(values[1]), float(values[2])
#
#                # Store line coordinates and color
#                lines_x.append(x_value)
#                lines_y.append(y_value)
#                lines_colors.append(current_color)

# Dump collected data into output file for debugging
with open(output_file_path, 'w') as output_file:
    output_file.write("Panel Size: {}\n".format(panel_size))
    output_file.write("Original Z Value: {}\n".format(original_z_value))
    output_file.write("Title: {}\n".format(title))
    output_file.write("Legend Entries: {}\n".format(legend_entries))
    output_file.write("Legend Colors: {}\n".format(legend_colors))
    output_file.write("Lines X: {}\n".format(lines_x))
    output_file.write("Lines Y: {}\n".format(lines_y))
    output_file.write("Lines Colors: {}\n".format(lines_colors))
    output_file.write("Arc Radii: {}\n".format(arcs_radii))
    output_file.write("Arcs Direction: {}\n".format(arcs_directions))

# Draw rectangle using Matplotlib
fig, ax = plt.subplots()
rectangle = Rectangle((0, 0), panel_size[0], panel_size[1], edgecolor='black', linewidth=1, facecolor='none')
ax.add_patch(rectangle)

# Plot lines with colors based on conditions
for color, label in zip(legend_colors, legend_entries):
    ax.plot([], [], marker='o', color=color, label=label)

# Plot lines with colors based on conditions
for i in range(len(lines_x) - 1):
    x_values = [lines_x[i], lines_x[i + 1]]
    y_values = [lines_y[i], lines_y[i + 1]]
    color = lines_colors[i + 1]
    ax.plot(x_values, y_values, color=color, linewidth=1)

# Set plot limits based on panel size
ax.set_xlim(-500, panel_size[0] + 500)
ax.set_ylim(-500, panel_size[1] + 500)

# Set plot title
plt.title(title)

# Show the legend
ax.legend()

# Show the plot
plt.show()
