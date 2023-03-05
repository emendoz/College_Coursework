/****************************************************************
 * Assignment: Project1 - An HTML Writer                        *
 * Filename: main.js                                            *
 * Author: Erika G. Mendoza                                     *
 * Date: January 30th, 2023                                     *
 * Description: This is a javascript file that outputs html     *
 * code that generates a table filled with courses from the     *
 * Sonoma State University Computer Science department.         *
 ***************************************************************/

const coursesFile = require(`./courses_studentView_2223_ComputerScience.json`);

console.log('<!DOCTYPE html>');
console.log('<html lang="en">');
console.log('<head>');
console.log('<meta charSet="UTF-8">');

// styling table
console.log('<style>');
console.log('table, th, td {');
console.log('border-top: 1pt solid lightgrey;');
console.log('border-bottom: 1pt solid lightgrey;');
console.log('border-collapse: collapse;');
console.log('font-family: "Lato Extended","Lato","Helvetica Neue",Helvetica,Arial,sans-serif;');
console.log('padding: 20px;');
console.log('}');
console.log('table {');
console.log('border: 1pt solid lightgrey;');
console.log('}');
console.log('th {');
console.log('color: #808080;');
console.log('font-weight: normal;');
console.log('text-align: left;');
console.log('background-color: white;');
console.log('}');
console.log('tbody:nth-child(odd) {');
console.log('background-color: #f2f2f2;');
console.log('}');
console.log('</style>');

console.log('<title>An HTML Writer</title>');
console.log('</head>');

console.log('<table>'); // start table

// top row headers
console.log('<thead>');
console.log('<tr>');
console.log('<th scope="col"> Course </th>');
console.log('<th scope="col"> Title </th>');
console.log('<th scope="col"> Units </th>');
console.log('<th scope="col"> Section </th>');
console.log('<th scope="col"> Component </th>');
console.log('<th scope="col"> Instructor </th>');
console.log('<th scope="col"> Meeting Pattern </th>');
console.log('<th scope="col"> Start Time </th>');
console.log('<th scope="col"> End Time </th>');
console.log('<th scope="col"> Classroom </th>');
console.log('</tr>');
console.log('</thead>');

// Course Row creations
for (let key in coursesFile) {

    for (let i in coursesFile[key]) {

        let subj = coursesFile[key]['subject'];
        let catalog = coursesFile[key]['catalog'];
        let classNum = coursesFile[key]['class_number'];

        if (i === "DIS" || i === "LAB" || i === "SUP" || i === "ACT" || i === "SEM" || i === "LEC") {
            let comps = coursesFile[key]['components'];

            if (comps.length === 2 && catalog !== '101' && classNum !== 2508) { // Courses with 2 sections
                if (i === "LAB") {
                    console.log('<tbody>');
                    console.log('<tr>');
                    console.log('<td rowspan="2">', subj, catalog, '</td>');
                    console.log('<td rowspan="2">', coursesFile[key]['course_title'], '</td>');
                    console.log('<td rowspan="2">', coursesFile[key]['units'], '</td>');
                    console.log('<td>', coursesFile[key]['DIS']['section'], '</td>');
                    console.log('<td>', coursesFile[key]['DIS']['component'], '</td>');
                    for (let j in coursesFile[key]['DIS']['instructors']) {
                        console.log('<td>', coursesFile[key]['DIS']['instructors'][j]['instructor_lName'] + ", " + coursesFile[key]['DIS']['instructors'][j]['instructor_fName'], '</td>');
                    }
                    for (let mt in coursesFile[key]['DIS']['meeting_pattern']) {
                        console.log('<td>', coursesFile[key]['DIS']['meeting_pattern'][mt]['meeting_pattern'], '</td>');
                        console.log('<td>', coursesFile[key]['DIS']['meeting_pattern'][mt]['start_time'], '</td>');
                        console.log('<td>', coursesFile[key]['DIS']['meeting_pattern'][mt]['end_time'], '</td>');
                        console.log('<td>', coursesFile[key]['DIS']['meeting_pattern'][mt]['facility_name'], '</td>');
                    }
                    console.log('<tr>');
                    console.log('<td>', coursesFile[key]['LAB']['section'], '</td>');
                    console.log('<td>', coursesFile[key]['LAB']['component'], '</td>');
                    for (let j in coursesFile[key]['LAB']['instructors']) {
                        console.log('<td>', coursesFile[key]['LAB']['instructors'][j]['instructor_lName'] + ", " + coursesFile[key]['LAB']['instructors'][j]['instructor_fName'], '</td>');
                    }
                    for (let mt in coursesFile[key]['LAB']['meeting_pattern']) {
                        console.log('<td>', coursesFile[key]['LAB']['meeting_pattern'][mt]['meeting_pattern'], '</td>');
                        console.log('<td>', coursesFile[key]['LAB']['meeting_pattern'][mt]['start_time'], '</td>');
                        console.log('<td>', coursesFile[key]['LAB']['meeting_pattern'][mt]['end_time'], '</td>');
                        console.log('<td>', coursesFile[key]['LAB']['meeting_pattern'][mt]['facility_name'], '</td>');
                    }
                    console.log('</tr>');
                    console.log('</tbody>');
                } else if (i === "DIS" && coursesFile[key]['catalog'] === "285") {
                    console.log('<tbody>');
                    console.log('<tr>');
                    console.log('<td rowspan="2">', subj, catalog, '</td>');
                    console.log('<td rowspan="2">', coursesFile[key]['course_title'], '</td>');
                    console.log('<td rowspan="2">', coursesFile[key]['units'], '</td>');
                    console.log('<td>', coursesFile[key]['DIS']['section'], '</td>');
                    console.log('<td>', coursesFile[key]['DIS']['component'], '</td>');
                    console.log('<td>', coursesFile[key]['DIS']['instructors'][1]['instructor_lName']+ ", " + coursesFile[key]['DIS']['instructors'][1]['instructor_fName'], '</td>');
                    console.log('<td>', coursesFile[key]['DIS']['meeting_pattern'][0]['meeting_pattern'], '</td>');
                    console.log('<td>', coursesFile[key]['DIS']['meeting_pattern'][0]['start_time'], '</td>');
                    console.log('<td>', coursesFile[key]['DIS']['meeting_pattern'][0]['end_time'], '</td>');
                    console.log('<td>', coursesFile[key]['DIS']['meeting_pattern'][0]['facility_name'], '</td>');
                    console.log('<tr>');
                    console.log('<td>', coursesFile[key]['DIS']['section'], '</td>');
                    console.log('<td>', coursesFile[key]['DIS']['component'], '</td>');
                    console.log('<td>', coursesFile[key]['DIS']['instructors'][1]['instructor_lName']+ ", " + coursesFile[key]['DIS']['instructors'][1]['instructor_fName'], '</td>');
                    console.log('<td>', coursesFile[key]['DIS']['meeting_pattern'][0]['meeting_pattern'], '</td>');
                    console.log('<td>', coursesFile[key]['DIS']['meeting_pattern'][0]['start_time'], '</td>');
                    console.log('<td>', coursesFile[key]['DIS']['meeting_pattern'][0]['end_time'], '</td>');
                    console.log('<td>', coursesFile[key]['DIS']['meeting_pattern'][0]['facility_name'], '</td>');
                    console.log('</tr>');
                    console.log('</tbody>');
                }
            } else if (comps.length === 1) { // Courses with one section
                console.log('<tbody>');
                console.log('<tr>');
                console.log('<td>', subj, catalog, '</td>');
                console.log('<td>', coursesFile[key]['course_title'], '</td>');
                console.log('<td>', coursesFile[key]['units'], '</td>');
                console.log('<td>', coursesFile[key][i]['section'], '</td>');
                console.log('<td>', coursesFile[key][i]['component'], '</td>');
                for (let j in coursesFile[key][i]['instructors']) {
                    if (coursesFile[key][i]['instructors'][j]['instructor_lName'] !== null) {
                        console.log('<td>', coursesFile[key][i]['instructors'][j]['instructor_lName'] + ", " + coursesFile[key][i]['instructors'][j]['instructor_fName'], '</td>');
                    } else {
                        console.log('<td></td>');
                    }
                }
                for (let mt in coursesFile[key][i]['meeting_pattern']) {
                    console.log('<td>', coursesFile[key][i]['meeting_pattern'][mt]['meeting_pattern'], '</td>');
                    if (coursesFile[key][i]['meeting_pattern'][mt]['start_time'] !== null) {
                        console.log('<td>', coursesFile[key][i]['meeting_pattern'][mt]['start_time'], '</td>');
                        console.log('<td>', coursesFile[key][i]['meeting_pattern'][mt]['end_time'], '</td>');
                    } else {
                        console.log('<td></td>');
                        console.log('<td></td>');
                    }
                    if (coursesFile[key][i]['meeting_pattern'][mt]['facility_name'] !== null) {
                        console.log('<td>', coursesFile[key][i]['meeting_pattern'][mt]['facility_name'], '</td>');
                    } else {
                        console.log('<td></td>');
                    }
                }
                console.log('</tr>');
                console.log('</tbody>');
            }
        }
    }
}
console.log('</table>');
console.log('</html>');