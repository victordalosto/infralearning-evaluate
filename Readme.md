<h1 align="center"> Infralearning - evaluate </h1>

This program is part of the <a ref="https://github.com/victordalosto/infralearning">Infralearning</a> project, an AI program used to evaluate the assets of Road Network.

This program is the final step in the project and is used to <b>Evaluate</b> the filming of roads, <strong>predicting</strong> and <strong>classificating </strong> its assets using AI trained models, created with a <a href=https://github.com/victordalosto/infralearning-engine>engine</a>.
<br/><br/>


<h2> How it works </h2>

This evaluation works in the following steps:

<li>Extracting the frames of a video and placing them in the mount directory</li>
<li>The program will use the first layer, the <strong>detection</strong> model, to evaluate if the assets are present or not</li>
<li>If the asset is present, the second layer of the model, specialized in <strong>classification</strong>, will classify the asset in one of the trained categories.</li>
<li>Further layers make more specialized classifications, such as: evaluating the quality of the asset and so forth.</li>

<br>

The program was created and intended to be used with docker, where each container would be loaded with (i) a mount directory and a video to be evaluated, (ii) the program would extract the frames and evaluate them with the AI models, (iii) and finally the results would be saved in the mount directory and the container could be destroyed.

<i>The docker part is not implemented yet.</i>


<h2> Example of usage</h2>

Tests were used to evaluate <strong>road signs</strong> following those steps:

(i) An MP4 video '<i>path_video</i>' is placed in the <b>main.py</b>;

(ii) On start, the program will create a <b>mount</b> directory where it will place the frames extracted;

(iii) The program will <b>detect</b> in each frame if a sign is present or not;

(iv) The frames with roads signs are classified in the following categoryes: <i>'advertencia', 'educativa', 'indicativa', 'regulamentacao', 'servicos', 'turistico'</i>

(v) The road signs can be classified in <b>quality</b> categories: <i>'boa', 'ruim', 'regular'</i> (not implemented yet)

(vi) The program will save the results in the <b>mount</b> directory, in the <i>results.

(vii) The program should generate a KML geographical file with the results (not implemented yet)