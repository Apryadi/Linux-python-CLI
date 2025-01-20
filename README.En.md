# CLI-Craft

A Minecraft-themed Command Line Interface built with Python that allows you to navigate and manipulate your file system using Minecraft-style commands.

```
 ██████╗██╗     ██╗      ██████╗██████╗  █████╗ ███████╗████████╗
██╔════╝██║     ██║     ██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
██║     ██║     ██║     ██║     ██████╔╝███████║█████╗     ██║   
██║     ██║     ██║     ██║     ██╔══██╗██╔══██║██╔══╝     ██║   
╚██████╗███████╗██║     ╚██████╗██║  ██║██║  ██║██║        ██║   
 ╚═════╝╚══════╝╚═╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝   
```

## Description

CLI-Craft transforms your regular command line interface into a Minecraft-themed experience. Navigate through directories as if you're exploring Minecraft worlds, create and delete files as if you're placing and mining blocks, and manage your file system with familiar Minecraft commands.

## Features

- Minecraft-style command system using `/` prefix
- ASCII art interface
- Achievement system
- File and directory manipulation using Minecraft terminology
- Tree view of directory structure
- File search functionality
- Size-based file finder

## Requirements

- Python 3.6 or higher
- Operating System: Windows, Linux, or MacOS

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cli-craft.git
```

2. Navigate to the project directory:
```bash
cd cli-craft
```

3. Run the script:
```bash
python cli_craft.py
```

## Commands

| Command | Description | Original CLI Equivalent |
|---------|-------------|------------------------|
| `/look` | Show files in current directory | `ls` |
| `/tp <location>` | Change directory | `cd` |
| `/coords` | Show current path | `pwd` |
| `/build <struct>` | Create directory | `mkdir` |
| `/destroy` | Remove directory | `rmdir` |
| `/place <block>` | Create file | `touch` |
| `/dig <block>` | Delete file | `rm` |
| `/clone` | Copy file | `cp` |
| `/move` | Move file | `mv` |
| `/clear` | Clear screen | `clear` |
| `/map` | Show directory tree | `tree` |
| `/find <item>` | Search files | `find` |
| `/large <size>` | Find large files | - |
| `/achievement` | Show random achievement | - |
| `/help` | Show help message | `help` |
| `/quit` | Exit CLI-Craft | `exit` |

## Usage Examples

1. Navigate to a directory:
```bash
World: /home/user /> /tp Documents
```

2. List files in current directory:
```bash
World: /home/user/Documents /> /look
```

3. Create a new directory:
```bash
World: /home/user/Documents /> /build NewWorld
```

4. Create a new file:
```bash
World: /home/user/Documents /> /place my_block.txt
```

5. Copy a file:
```bash
World: /home/user/Documents /> /clone source.txt backup/source.txt
```

## Error Handling

CLI-Craft provides clear error messages for common issues:
- File/directory not found
- Permission denied
- Invalid commands
- Missing arguments

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by Minecraft's command system
- Built using Python's standard library
- ASCII art generated for CLI-Craft interface

## Future Improvements

- [ ] Add configuration file support
- [ ] Implement file content editing
- [ ] Add more Minecraft-themed features
- [ ] Create custom themes
- [ ] Add multiplayer support
- [ ] Implement file permissions management
- [ ] Add command history

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.
