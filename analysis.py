with open("LeMieAttività.html") as data:
    channels_likes = {}

    line_counter = 0
    control_string = '<a href="https://www.youtube.com/channel/'

    for line in data:
        line_counter += 1
        strings_in_line = line.count(control_string)
        pointer_in_line = 0

        for k in range(strings_in_line):
            string_position = line.find(control_string, pointer_in_line)

            output = line[string_position + 67 : string_position + 500]
            stopping_point = output.find("<")
            channel_name = output[:stopping_point]

            if channel_name in channels_likes:
                channels_likes[channel_name] += 1
            else:
                channels_likes[channel_name] = 1

            pointer_in_line = string_position + 1

sorted_channels = {}

for channel in sorted(channels_likes, key=channels_likes.get, reverse=True):
    sorted_channels[channel] = channels_likes[channel]

with open("likes.txt", "w") as out:
    for channel in sorted_channels:
        out.write(channel + " - " + str(sorted_channels[channel]) + "\n")

total_likes = 0

for channel in sorted_channels:
    total_likes += sorted_channels[channel]

print(total_likes)
