% ========= = arr=======================================
% Visual Search Task Data Analysis Pipeline
% ==================================================

% Raw data file name
file = '/Users/stan.park712/Library/CloudStorage/Box-Box/jp464/Neuro378/projectFiles/data/vstData_anon.xlsx';
subjectNum = 8; 
e = 1;

circleA_T = process(subjectNum, 'circleA', file, e);
circleB_T = process(subjectNum, 'circleB', file, e);
orientation_T = process(subjectNum, 'orientation', file, e);
 
% Matrix view of complete averaged table
circleA_M = table2array(circleA_T);
circleB_M = table2array(circleB_T);
orientation_M = table2array(orientation_T);

% Average of all subjects 
circleA_avgM = mean(circleA_M, 1, 'omitnan');
circleB_avgM = mean(circleB_M, 1, 'omitnan');
orientation_avgM = mean(orientation_M, 1, 'omitnan');

mean(circleA_avgM)
mean(circleB_avgM)
mean(orientation_avgM)

% Plot data
distractors = 1:6;
plot(distractors, circleA_avgM, 'bx')
hold on
plot(distractors, circleB_avgM, 'gx')
plot(distractors, orientation_avgM, 'rx')

mdl_circleA = fitlm(distractors, circleA_avgM);
mdl_circleB = fitlm(distractors, circleB_avgM);
% mdl_orientation = fitlm(distractors, orientation_avgM);
mdl_orientation = fitlm(distractors(2:length(distractors)), orientation_avgM(2: length(orientation_avgM)));

display("task1 lm summary");
mdl_circleA
display("task2 lm summary");
mdl_circleB
display("task3 lm summary");
mdl_orientation

p_circleA = plot(mdl_circleA)
p_circleB = plot(mdl_circleB)
p_orientation = plot(mdl_orientation)
set(p_circleA(1), 'Color', 'b');
set(p_circleA(2), 'Color', 'b');
set(p_circleA(3), 'Color', 'b');
set(p_circleA(4), 'Color', 'b');

set(p_circleB(1), 'Color', 'g');
set(p_circleB(2), 'Color', 'g');
set(p_circleB(3), 'Color', 'g');
set(p_circleB(4), 'Color', 'g');

set(p_orientation(1), 'Color', 'r');
set(p_orientation(2), 'Color', 'r');
set(p_orientation(3), 'Color', 'r');
set(p_orientation(4), 'Color', 'r');
legend([p_circleA(2), p_circleB(2), p_orientation(2)], 'task1', 'task2', 'task3')

hold off
title("Search Time for Varying Number of Features");
xlabel("Number of features");
ylabel("Search time (sec)");

% [p, tbl, stats] = anova1(circleA_M);
% [p, tbl, stats] = anova1(circleB_M);
% [p, tbl, stats] = anova1(orientation_M);
% orientation_M(:, 1) = [];
% [p, tbl, stats] = anova1(orientation_M);



function proT = process(subjectNum, task, file, e)
    % Construct processed table 
    id = [];
    col1 = [];
    col2 = [];
    col3 = [];
    col4 = [];
    col5 = [];
    col6 = [];
    proT = table(col1, col2, col3, col4, col5, col6);
    
    % Add average values for each subject into table
    for i = 1:subjectNum
        if i < 10
            id = strcat('0', int2str(i), task);
        else
            id = strcat(int2str(i), task);
        end
    
        rawT = readtable(file, 'sheet', id);
        rawT.(1) = [];
        append = addT(rawT, 1, width(rawT) - 1, [], e);
        proT = [proT; num2cell(append)];
    end
end


% Find the average time for each column
function avg = average(T, i, e)
    T = T(:, i:i+1);
    T = T((T.(2) == e & T.(1) ~= 0), 1);
    avg = mean(T.(1), 'omitnan');
end

% Find array of average values for each subject
function ret = addT(T, initial, final, array, e)
    for i = initial:2:final
        array(end + 1) = average(T, i, e);
        ret = array; 
    end
end


    


    
    




