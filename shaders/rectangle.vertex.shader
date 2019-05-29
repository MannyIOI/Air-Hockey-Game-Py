#version 330 core
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 newColor;

// create a vec2 variable that holds the dx and dy value
uniform vec2 dPos = vec2(0, 0);

out vec3 color;

void main()
{
	// add the dx and dy values to the original position
	gl_Position = vec4(position.x + dPos[0], position.y + dPos[1], position.z, 1.0);
	color = newColor;
}