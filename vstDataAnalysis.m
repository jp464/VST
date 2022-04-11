% ========= = arr=======================================
% Visual Search Task Data Analysis Pipeline
% ==================================================

% Raw data file name
file = '/Users/stan.park712/Library/CloudStorage/Box-Box/jp464/Neuro378/projectFiles/data/vstData_anon.xlsx';
subjectNum = 3;

% e = 1;
e = 0;

circleA_T = process(subjectNum, 'circleA', file, e)
circleB_T = process(subjectNum, 'circleB', file, e)
orientation_T = process(subjectNum, 'orientation', file, e)

    
% Matrix view of complete averaged table
circleA_M = table2array(circleA_T);
circleB_M = table2array(circleB_T);
orientation_M = table2array(orientation_T);

% Average of all subjects 
circleA_avgM = mean(circleA_M, 1);
circleB_avgM = mean(circleB_M, 1);
orientation_avgM = mean(orientation_M, 1);

% Plot data
distractors = 1:length(proM);
plot(distractors, circleA_avgM, 'bx')
hold on
plot(distractors, circleB_avgM, 'gx')
plot(distractors, orientation_avgM, 'rx')

p1 = polyfit(distractors, circleA_avgM, 1);
x1 = linspace(0, 6);
y1 = polyval(p1, x1);

p2 = polyfit(distractors, circleB_avgM, 1);
x2 = linspace(0, 6);
y2 = polyval(p2, x1);

p3 = polyfit(distractors, orientation_avgM, 1);
x3 = linspace(0, 6);
y3 = polyval(p3, x1);

plot(x1, y1, 'blue');
plot(x2, y2, 'green');
plot(x3, y3, 'red');
hold off
title("Search Time for Varying Number of Distractors");
xlabel("Number of distractors");
ylabel("Search time (sec)");

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
    avg = mean(T.(1));
end

% Find array of average values for each subject
function ret = addT(T, initial, final, array, e)
    for i = initial:2:final
        array(end + 1) = average(T, i, e);
        ret = array; 
    end
end


    


    
    




