// import { useMemo } from 'react';
import { Calendar } from 'react-big-calendar';

import 'react-big-calendar/lib/css/react-big-calendar.css';

const culture = 'ru';


// eslint-disable-next-line react/prop-types
export function CalendarBlock({ localizer, date, formats, dayPropGetter }) {
  // const {views} = useMemo(() => ({views:[Views.MONTH],}),[]);
  return (
		<Calendar
      onDrillDown={()=>((0))}
			formats={formats}
			culture={culture}
			localizer={localizer}
			toolbar={false}
			date={date}
			dayPropGetter={dayPropGetter}
			style={{ height: 300, margin: 0, padding: 0, width: 300 }}
		/>
	);
}
