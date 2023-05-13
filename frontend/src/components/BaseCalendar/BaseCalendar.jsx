import { React, useMemo } from 'react';
import PropTypes from 'prop-types';
import { Calendar } from 'react-big-calendar';
import styles from './BaseCalendar.module.css';

const culture = 'ru';

export function BaseCalendar({ localizer }) {
	const { defaultDate, formats } = useMemo(
		() => ({
			defaultDate: new Date(),
			formats: {
				weekdayFormat: (date) => localizer.format(date, 'eeeeee', culture),
			},
		}),
		[localizer]
	);

	return (
		<Calendar
			defaultDate={defaultDate}
			localizer={localizer}
			startAccessor="start"
			endAccessor="end"
			culture={culture}
			formats={formats}
			events={[]}
			className={styles.calendar}
			messages={{
				date: 'Дата',
				time: 'Время',
				event: 'Событие',
				allDay: 'Весь день',
				week: 'Неделя',
				work_week: 'Рабочая неделя',
				day: 'День',
				month: 'Месяц',
				previous: 'Назад',
				next: 'Вперёд',
				yesterday: 'Вчера',
				tomorrow: 'Завтра',
				today: 'Сегодня',
				agenda: 'Сводка',
			}}
		/>
	);
}

BaseCalendar.propTypes = {
	localizer: PropTypes.element.isRequired,
};
