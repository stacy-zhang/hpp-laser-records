# HPP Laser Records

A small dataset and visualization toolkit for high-peak-power laser systems around the world. It collects published specifications for notable laser facilities and provides two ways to explore them:

- An **interactive scatter plot** of peak power vs. wavelength.
- A **searchable data table** served as a web app.

## Dataset

[`laser_systems.csv`](laser_systems.csv) contains one row per laser system with the following columns:

| Column | Description |
| --- | --- |
| `name` | Name of the laser system or facility. |
| `location` | City and country of the institution. |
| `peak_power(W)` | Peak power in watts. Where unavailable, estimated as pulse energy / pulse duration. |
| `wavelength(µm)` | Operating wavelength in micrometers. |
| `repetition_rate(Hz)` | Pulse repetition rate in hertz (some values are estimates, see `notes`). |
| `year` | Year of the reference or reported result. |
| `references` | Source publications, DOIs, or facility pages. |
| `notes` | Caveats and clarifications (e.g. estimated values). |

## Scripts

### `plot.py` — Peak power vs. wavelength scatter plot

Renders an interactive Matplotlib scatter plot where:

- **x-axis** is wavelength (µm) and **y-axis** is peak power (W, log scale with SI-prefixed labels).
- **Marker color** encodes the decade of the reported result.
- **Marker size** scales with repetition rate (logarithmically).
- **Hovering** over a point shows the system name, institution, and DOI/reference.

### `table.py` — Searchable data table

A [Streamlit](https://streamlit.io/) app that displays the full dataset in a table with:

- A text search box that filters systems by name.
- Clickable links rendered from the `references` column.

## Getting started

### Prerequisites

- Python 3.9+

### Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/stacy-zhang/hpp-laser-records.git
cd hpp-laser-records
pip install numpy pandas matplotlib streamlit
```

### Usage

Show the interactive scatter plot:

```bash
python plot.py
```

Launch the searchable table app:

```bash
streamlit run table.py
```

## Contributing

To add or update a laser system, edit [`laser_systems.csv`](laser_systems.csv) and include a reference (DOI or facility page) in the `references` column. Note any estimated values in the `notes` column.
