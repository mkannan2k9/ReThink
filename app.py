from flask import Flask, render_template, request, redirect, url_for
from google import genai
import os
import markdown
import re

app = Flask(__name__)

#genai.configure(api_key='AIzaSyA635wowrHfFJgkS4MWQbEIXrHIkerxnCA')
client = genai.Client(api_key= "AIzaSyA635wowrHfFJgkS4MWQbEIXrHIkerxnCA")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        incident_detail = request.form.get('incident_detail', '')
        student_reaction = request.form.get('student_reaction', '')
        is_regretting = request.form.get('is_regretting', '')
        how_regretting = request.form.get('how_regretting', '')

        # Create prompt for Gemini
        prompt = f"""
        Analyze the following student incident and provide counseling advice:

        Incident Details: """+incident_detail+"""
        Student's Reaction: """+student_reaction+"""
        Is the student regretting: """+is_regretting+"""
        How the student is regretting (if applicable): """+how_regretting+"""

        Please structure your output in the following response:
        1. Empathetic reflection on the user's situation or feelings. This must not be over 25 words.
        2. An analysis of the student and how the student could have reacted better.
        3. If the student is regretting, acknowlege it and if the student has specified how he is regretting, encourage him, tell him there by provind some words of encouragements.
        4. If the situation is too serious, suggestions or therapeutic approaches that might be helpful.
        5. Next action steps: A few thing the student can implement in his/her life to make sure the student does not repeat this. DO NOT HAVE ANY POINTS SAYING THAT AFTER THIS APPROACH YOUR TEACHER, ETC. Imagine you are the student's counsellor.
        
        Do not give your outputs with bullet points. It must be in paragraphs, and it must be proffessional. Structure the paragraphs under relevant headings. Use formattings such as bold, italics, and underline to make it look better.

        Keep the response empathetic, constructive, and focused on helping the student learn and grow from this experience.
        """
        prompt1 = """This is the information about an incident that took place in a student's life. Effectively summarise it:
        Incident Details: """+incident_detail+"""
            Student's Reaction: """+student_reaction+"""
            Is the student regretting: """+is_regretting+"""
            How the student is regretting (if applicable): """+how_regretting+"""
        Keep these in mind:
        1. The summary must not be over one paragraph.
        2. The summary must effectively summarise what incident took place. Focus on giving a brief on the details of the incident, the student's reaction, if the student is regretting it and how the student is regretting it.
        3. Output only the summary. No introduction, no 'support for styudent', no 'next steps'. Only summary. no heading also. ONLY THE SUMMARY OF THE INCIDENT."""

        try:
            # Generate response from Gemini
            response = client.models.generate_content(model = "gemini-2.0-flash", contents = prompt)
            gemini_output = response.text
            response1 = client.models.generate_content(model = "gemini-2.5-flash", contents = prompt1)
            gemini_output1 = response1.text
            gemini_output = re.sub(r'\n{3,}', '\n\n', gemini_output)
            gemini_output1 = re.sub(r'\n{3,}', '\n\n', gemini_output1)
            html_content1 = markdown.markdown(gemini_output, extensions=['extra', 'fenced_code', 'tables'])
            html_content2 = markdown.markdown(gemini_output1, extensions=['extra', 'fenced_code', 'tables'])

            # Redirect to results page with data
            return render_template('result.html', 
                                 summary = html_content2,
                                 gemini_output=html_content1)
        except Exception as e:
            error_message = f"Error generating response: {str(e)}"
            return render_template('result.html', error=error_message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
