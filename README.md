<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/KarthikUdyawar/Conway-s-Game-of-Life">
    <img src="images/icon.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Conway's Game of Life</h3>

  <p align="center">
    The Game of Life is a cellular automaton and a zero-player game.
    <br />
    <a href="https://github.com/KarthikUdyawar/Conway-s-Game-of-Life"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/KarthikUdyawar/Conway-s-Game-of-Life">View Demo</a>
    ·
    <a href="https://github.com/KarthikUdyawar/Conway-s-Game-of-Life/issues">Report Bug</a>
    ·
    <a href="https://github.com/KarthikUdyawar/Conway-s-Game-of-Life/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Gif of Conway's Game of Life][product-screenshot]](https://github.com/KarthikUdyawar/Conway-s-Game-of-Life/blob/main/screenshot/cover.gif)

Conway's Game of life is by far the most famous cellular automaton. It is best example of how many simple thing can work thoughts to create something complex. If almost fells like real life

### Rules of Game of life

- **Overpopulation**: A cell dies(_off_) if its surrounded by more than three living cells.

- **Static**: A cell lives(_on_) if its surrounded by two or three living cells.

- **Underpopulated**: A cell dies(_off_) if its surrounded by fewer than two living cells.

- **Reproduction**: A cell becomes live(_on_) if a dead cell is surrounded by exactly three cells.

### Built With

- [Python](https://www.python.org/)
- [Pygame](https://www.pygame.org/news)

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

List things you need to use the software and how to install them.

- Python >= 3.8
  ```sh
  python --version
  # Python 3.8.0
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/KarthikUdyawar/Conway-s-Game-of-Life.git
   ```
2. To install requirement packages
   ```sh
   pip install -r requirements.txt
   ```

### Run

- To run the code
  ```sh
   python main.py
  ```

<!-- USAGE EXAMPLES -->

## Usage

|       Key       |        Action        |
| :-------------: | :------------------: |
|     `Enter`     |  Toggle pause time   |
| `Click or Drag` | Toggle cell's state  |
|       `R`       | Generate random seed |
|       `C`       |        Clear         |
|       `S`       |         Save         |
|       `L`       |         Load         |

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/KarthikUdyawar/Conway-s-Game-of-Life/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Project Link: [https://github.com/KarthikUdyawar/Conway-s-Game-of-Life](https://github.com/KarthikUdyawar/Conway-s-Game-of-Life)

## Acknowledgements

- [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
- [Scholarpedia](http://www.scholarpedia.org/article/Game_of_Life)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username
[product-screenshot]: screenshot/cover.gif
