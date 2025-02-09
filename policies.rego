package access_control

# Default is deny access
default allow = false

allow if {
    input.username in data.github_data.repos[input.repository_name].collaborators
}
allow if {
    data.github_data.repos[input.repository_name].collaborators[input.username].admin == true
}