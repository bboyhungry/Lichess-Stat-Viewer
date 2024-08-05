import React from 'react';

interface SearchBarProps {
    username: string;
}

const SearchBar: React.FC<SearchBarProps> = (props: SearchBarProps) => {
    const { username } = props
    return (
    <input
        type="text"
        placeholder="Search here"
        onChange={() => {}}
        value={username} />
    );
}

export default SearchBar;