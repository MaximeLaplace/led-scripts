import React, { useState } from 'react';

import { TextField } from '@mui/material';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import { width } from '@mui/system';

type Props = {
	confirmAction: (password: string) => () => void;
	handleClose: () => void;
	open: boolean;
};

const ConfirmationDialogGenerator = ({
	confirmAction,
	handleClose,
	open
}: Props) => {
	const [password, setPassword] = useState<string>('');

	const handlePasswordInput = (
		event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
	) => {
		setPassword(event.currentTarget.value);
	};

	return (
		<div>
			<Dialog
				open={open}
				onClose={handleClose}
				aria-labelledby="alert-dialog-title"
				aria-describedby="alert-dialog-description"
			>
				<DialogTitle>
					<h3>Reboot site</h3>
				</DialogTitle>
				<DialogContent>
					<DialogContentText>
						Are you sure you want to reboot the website?
						<br />
						This will trigger pulling latest changes and might take few seconds.
						<br />
						You will have to reload this page.
						<br />
						<br />
						<div
							style={{
								display: 'flex',
								flexDirection: 'row',
								gap: '20px',
								alignItems: 'center'
							}}
						>
							<h3>Password: </h3>
							<TextField
								sx={{
									flexGrow: '1'
								}}
								label="Password"
								id="outlined-size-small"
								size="small"
								onChange={handlePasswordInput}
								value={password}
							/>
						</div>
					</DialogContentText>
				</DialogContent>
				<DialogActions>
					<Button onClick={handleClose}>Cancel</Button>
					<Button
						onClick={() => {
							confirmAction(password)();
							handleClose();
						}}
						variant="contained"
					>
						Reboot
					</Button>
				</DialogActions>
			</Dialog>
		</div>
	);
};

export const useRebootDialog = (
	confirmAction: (password: string) => () => void
) => {
	const [open, setOpen] = useState<boolean>(false);

	const handleOpen = () => setOpen(true);
	const handleClose = () => setOpen(false);
	const toggleOpen = () => setOpen((current) => !current);

	const ConfirmationDialog = () => (
		<ConfirmationDialogGenerator
			open={open}
			handleClose={handleClose}
			confirmAction={confirmAction}
		></ConfirmationDialogGenerator>
	);

	return {
		ConfirmationDialog,
		handleClose,
		handleOpen,
		open,
		toggleOpen
	};
};
