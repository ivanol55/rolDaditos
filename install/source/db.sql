--
-- PostgreSQL database dump
--

-- Dumped from database version 11.7 (Debian 11.7-0+deb10u1)
-- Dumped by pg_dump version 11.7 (Debian 11.7-0+deb10u1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: campaigns; Type: TABLE; Schema: public; Owner: roldaditos
--

CREATE TABLE public.campaigns (
    campaign text NOT NULL
);


ALTER TABLE public.campaigns OWNER TO REPLACEONINSTALL;

--
-- Name: personajes; Type: TABLE; Schema: public; Owner: roldaditos
--

CREATE TABLE public.personajes (
    personaje text NOT NULL,
    campaignpersonaje text
);


ALTER TABLE public.personajes OWNER TO REPLACEONINSTALL;

--
-- Name: tiradas; Type: TABLE; Schema: public; Owner: roldaditos
--

CREATE TABLE public.tiradas (
    id integer NOT NULL,
    fechahora timestamp without time zone,
    sesion integer,
    dadotirado integer,
    nresultante integer,
    personaje text
);


ALTER TABLE public.tiradas OWNER TO REPLACEONINSTALL;

--
-- Name: tiradas_id_seq; Type: SEQUENCE; Schema: public; Owner: roldaditos
--

CREATE SEQUENCE public.tiradas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tiradas_id_seq OWNER TO REPLACEONINSTALL;

--
-- Name: tiradas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: roldaditos
--

ALTER SEQUENCE public.tiradas_id_seq OWNED BY public.tiradas.id;


--
-- Name: tiradas id; Type: DEFAULT; Schema: public; Owner: roldaditos
--

ALTER TABLE ONLY public.tiradas ALTER COLUMN id SET DEFAULT nextval('public.tiradas_id_seq'::regclass);


--
-- Name: tiradas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: roldaditos
--

SELECT pg_catalog.setval('public.tiradas_id_seq', 1, true);


--
-- Name: campaigns campaigns_pk; Type: CONSTRAINT; Schema: public; Owner: roldaditos
--

ALTER TABLE ONLY public.campaigns
    ADD CONSTRAINT campaigns_pk PRIMARY KEY (campaign);


--
-- Name: personajes personajes_pkey; Type: CONSTRAINT; Schema: public; Owner: roldaditos
--

ALTER TABLE ONLY public.personajes
    ADD CONSTRAINT personajes_pkey PRIMARY KEY (personaje);


--
-- Name: tiradas tiradas_pkey; Type: CONSTRAINT; Schema: public; Owner: roldaditos
--

ALTER TABLE ONLY public.tiradas
    ADD CONSTRAINT tiradas_pkey PRIMARY KEY (id);


--
-- Name: personajes personajes_fk; Type: FK CONSTRAINT; Schema: public; Owner: roldaditos
--

ALTER TABLE ONLY public.personajes
    ADD CONSTRAINT personajes_fk FOREIGN KEY (campaignpersonaje) REFERENCES public.campaigns(campaign);


--
-- Name: tiradas tiradas_personaje_fkey; Type: FK CONSTRAINT; Schema: public; Owner: roldaditos
--

ALTER TABLE ONLY public.tiradas
    ADD CONSTRAINT tiradas_personaje_fkey FOREIGN KEY (personaje) REFERENCES public.personajes(personaje);


--
-- PostgreSQL database dump complete
--

