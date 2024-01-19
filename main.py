import re
import matplotlib.pyplot as plt


def read_nc_file(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
    return content


def parse_coordinates(content):
    pattern = re.compile(r'G[01] X([-+]?\d*\.\d+) Y([-+]?\d*\.\d+)')
    title_pattern = re.compile(r'\(TOOL - (.*?)\)')

    coordinates = []
    current_tool = None
    current_group = []

    for line in content:
        match = pattern.search(line)
        title_match = title_pattern.search(line)

        if title_match:
            # Set the title for the plot
            current_tool = title_match.group(1)
            coordinates.append((current_tool, 'k', []))
            continue

        if match:
            current_group.append((current_tool, float(match.group(1)), float(match.group(2))))

    if current_tool is not None:
        coordinates[-1] = (current_tool, 'k', current_group)

    return coordinates


def write_coordinates_to_file(coordinates, output_file_path):
    with open(output_file_path, 'w') as file:
        for tool, _, points in coordinates:
            file.write(f"Tool - {tool}\n")
            for _, x, y in points:
                file.write(f"X: {x}, Y: {y}\n")
            file.write('\n')


def plot_coordinates(coordinates):
    fig, ax = plt.subplots()
    plt.axis('equal')  # Set equal aspect ratio

    title_set = False

    for tool, color, points in coordinates:
        if not points:
            # Skip empty points (no coordinates for this tool)
            continue

        if not title_set:
            ax.set_title(tool)  # Set the title
            title_set = True

        try:
            # Extract x and y coordinates only for valid points
            x, y = zip(*[(point[1], point[2]) for point in points])

            # Use a line instead of dots
            ax.plot(x, y, label=f'Tool - {tool}', color=color, marker='o', markersize=2, linestyle='-')
        except IndexError as e:
            print(f"Error processing Tool {tool}: {e}")
            print(f"Skipping Tool {tool} due to IndexError.")

    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

    try:
        plt.show()
    except KeyboardInterrupt:
        print("Plotting interrupted.")


if __name__ == "__main__":
    file_path = "09026417_001.nc"
    output_file_path = "coordinates_output.txt"

    nc_content = read_nc_file(file_path)
    coordinates = parse_coordinates(nc_content)
    write_coordinates_to_file(coordinates, output_file_path)
    plot_coordinates(coordinates)
    print(coordinates)
