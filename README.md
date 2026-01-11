# AI Student Counselor

***

An AI-powered web application designed to help students reflect on personal incidents, providing constructive analysis, empathy, and actionable counseling advice using Google's Gemini models.

**Owner:** Kannan Murugapandian  
**License:** MIT

***

## Features

- **Incident Analysis:** Users input details about an incident, their reaction, and feelings of regret.
- **AI-Powered Advice:**
  - **Empathetic Reflection:** Provides immediate validation of the student's feelings (under 25 words).
  - **Behavioral Analysis:** Analyzes reactions and suggests better alternatives.
  - **Encouragement:** Acknowledges regret and offers professional encouragement.
  - **Actionable Steps:** Offers concrete life changes to prevent recurrence, acting as a direct counselor.
- **Incident Summarizer:** Automatically generates a concise one-paragraph summary of the event for quick review.
- **Rich Formatting:** Outputs professional, structured advice with bolding, italics, and proper headings, rendered from Markdown to HTML.

***

## Requirements

- Python 3.8+
- **Google Gemini API Key**
- Python Packages:
  - `Flask`
  - `google-genai`
  - `markdown`

***

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mkannan2k9/ReThink.git
   cd ai-student-counselor
   ```

2. **Install dependencies:**
   ```bash
   pip install Flask google-genai markdown
   ```

3. **Configure API Key:**
   Open `app.py` (or the main flask file) and replace the placeholder:
   ```python
   client = genai.Client(api_key="YOUR_ACTUAL_API_KEY")
   ```

4. **Verify Templates:**
   Ensure you have a `templates` folder containing:
   - `index.html` (The input form)
   - `result.html` (The results display page)

***

## Usage

1. **Run the application:**
   ```bash
   python app.py
   ```

2. **Open in Browser:**
   Go to `http://localhost:5000/`

3. **Get Counseling:**
   - Fill out the form with details of an incident.
   - Click Submit.
   - The AI will generate a summary of what happened and a detailed, structured counseling session.

***

## Models Used

- **Gemini 2.0 Flash:** Used for the detailed counseling advice (Analysis, Empathy, Action Steps).
- **Gemini 2.5 Flash:** Used for the concise incident summary.

***

## License

MIT License

Copyright (c) 2025 Kannan Murugapandian

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

***

## Acknowledgements

- [Google Gemini API](https://ai.google.dev/)
- [Flask](https://flask.palletsprojects.com/)

***

**For questions or support, contact Kannan Murugapandian.**
